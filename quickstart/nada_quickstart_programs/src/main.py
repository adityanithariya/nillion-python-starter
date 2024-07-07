from nada_dsl import *

def nada_main():
  """
    This program calculates the final selling prices for a syringe at a hospital and a medical shop. 

    Inputs:
      * supplier_price: The base price of the syringe provided by the supplier (e.g., 100).
      * supplier_hospital_margin: The percentage margin the supplier keeps when selling to hospitals (e.g., 10).
      * supplier_medical_margin: The percentage margin the supplier keeps when selling to medical shops (e.g., 15).
      * hospital_margin: The percentage margin the hospital adds to the base price (e.g., 5).
      * medical_margin: The percentage margin the medical shop adds to the base price (e.g., 10).

    Outputs:
      * Hospital price: The price at which the hospital sells the syringe.
      * Medical shop price: The price at which the medical shop sells the syringe.
  """
  supplier = Party(name="supplier")
  hospital = Party(name="hospital")
  medical_shop = Party(name="medical_shop")
  customer = Party(name="customer")

  cyringe_base_price = SecretInteger(Input(name="cyringe_base_price", party=supplier))
  supplier_hospital_margin = SecretInteger(Input(name="supplier_hospital_margin", party=supplier))
  supplier_medical_margin = SecretInteger(Input(name="supplier_medical_margin", party=supplier))
  hundred = Integer(100)

  hospital_base_price = cyringe_base_price * hundred / (hundred - supplier_hospital_margin)
  hospital_margin = SecretInteger(Input(name="hospital_margin", party=hospital))
  hospital_price = hospital_base_price * hundred / (hundred - hospital_margin)

  medical_base_price = cyringe_base_price * hundred / (hundred - supplier_medical_margin)
  medical_margin = SecretInteger(Input(name="medical_margin", party=medical_shop))
  medical_price = medical_base_price * hundred / (hundred - medical_margin)

  return [
    Output(hospital_price, "cyringe_hospital_price", customer),
    Output(medical_price, "cyringe_medical_price", customer)
  ]

