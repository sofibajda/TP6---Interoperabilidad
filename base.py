import requests
from patient import create_patient_resource


# Enviar el recurso FHIR al servidor HAPI FHIR
def send_resource_to_hapi_fhir(resource,resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}"
    headers = {"Content-Type": "application/fhir+json"}
    resource_json = resource.json()


    response = requests.post(url, headers=headers, data=resource_json)

    if response.status_code == 201:
        print("Recurso creado exitosamente")
        
        # Devolver el ID del recurso creado
        return response.json()['id']
    else:
        print(f"Error al crear el recurso: {response.status_code}")
        print(response.json())
        return None

# Buscar el recurso por ID 
def get_resource_from_hapi_fhir(resource_id, resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}/{resource_id}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        resource = response.json()
        print(resource)
    else:
        print(f"Error al obtener el recurso: {response.status_code}")
        print(response.json())

# Búsqueda del recurso por identifier
def search_patient_by_identifier(document_number):
    
    url = f"http://hapi.fhir.org/baseR4/Patient?identifier={document_number}"
    headers = {"Accept": "application/fhir+json"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        bundle = response.json()
        if bundle.get('entry'):
            for entry in bundle['entry']:
                patient = entry['resource']
                print("Paciente encontrado:")
                print(patient)
                return patient['id']
        else:
            print("No se encontraron pacientes con ese documento.")
            return None
    else:
        print(f"Error al buscar el paciente: {response.status_code}")
        print(response.json())
        return None
