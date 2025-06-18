from fhir.resources.allergyintolerance import AllergyIntolerance
from fhir.resources.reference import Reference
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding


def create_allergy_intolerance(patient_id, substance=None, clinical_status="active"):
    # Crear el diccionario con los datos del recurso
    allergy_data = {
        "clinicalStatus": {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical",
                    "code": clinical_status,
                    "display": clinical_status.capitalize()
                }
            ]
        },
        "patient": {
            "reference": f"Patient/{patient_id}"
        },
        "code": {
            "coding": [
                {
                    "system": "http://snomed.info/sct",
                    "code": "91936005",  # Allergy to penicillin
                    "display": substance if substance else "Unknown substance"
                }
            ]
        }
    }

    # Crear el objeto AllergyIntolerance con los datos
    allergy = AllergyIntolerance(**allergy_data)
  
    return allergy

