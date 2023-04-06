from swagger_server.models.response_institution import ResponseInstitution
from swagger_server.models.response_institution_data import ResponseInstitutionData
from swagger_server.models.request_institution_add import RequestInstitutionAdd

class InstitutionUseCase:

    def __init__(self, institution_repository):
        self.institution_repository = institution_repository

    def get_institution(self):
        """
            Lista de instutition
        :return:
        """

        data_response = []
        institutions = self.institution_repository.get_institution()

        for i in institutions:
            data_response.append(
                ResponseInstitutionData(
                    id=i.id,
                    name=i.name,
                    description=i.description,
                    address=i.address,
                )
            )

        response = ResponseInstitution(
            code=0,
            message="proceso exitoso",
            data=data_response
        )

        return response

    def add_institution(self, body):
        """
            Lista de instutition
        :return:
        """
        val1 = self.institution_repository.add_institution(body)

        response = ResponseInstitution(
            code=0,
            message="proceso agregado con éxito",
            data=val1
        )

        return response

    def get_institution_by_id(self, institution_id):
        """
            Lista de instutition
        :return:
        """
        data_response = []
        institutions = self.institution_repository.get_institution_by_id(institution_id)

        for i in institutions:
            data_response.append(
                ResponseInstitutionData(
                    id=i.id,
                    name=i.name,
                    description=i.description,
                    address=i.address,
                )
            )

        if data_response:
            response = ResponseInstitution(
                code=0,
                message="proceso con exito",
                data=data_response
            )
        else:
            response = ResponseInstitution(
                code=0,
                message="No Registrado",
                data=data_response
            )

        return response
