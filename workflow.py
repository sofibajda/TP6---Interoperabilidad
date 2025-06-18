from patient import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir, search_patient_by_identifier
from allergy import create_allergy_intolerance

if __name__ == "__main__":
    # Parámetros del paciente (se puede dejar algunos vacíos)
    family_name = "Doe"
    given_name = "John"
    birth_date = "1990-01-01"
    gender = "male"
    phone = None 
    document_number = "42809201"

    # Crear y enviar el recurso de paciente
    patient = create_patient_resource(family_name, given_name, birth_date, gender, phone, document_number)
    patient_id = send_resource_to_hapi_fhir(patient, 'Patient')

    # Ver el recurso de paciente creado
    if patient_id:
        get_resource_from_hapi_fhir(patient_id,'Patient')

    # Busca el paciente por el número de pasaporte
    print("\nBuscando paciente por número de de documento...")
    search_patient_by_identifier(document_number)

    # Crea y envía el recurso AllergyIntolerance
    if patient_id:
        print("\nCreando recurso AllergyIntolerance...")
        allergy = create_allergy_intolerance(patient_id, substance="Penicillin")
        allergy_id = send_resource_to_hapi_fhir(allergy, 'AllergyIntolerance')

        # Vemos el recurso creado
        if allergy_id:
            get_resource_from_hapi_fhir(allergy_id, 'AllergyIntolerance')