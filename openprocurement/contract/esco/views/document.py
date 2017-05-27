# -*- coding: utf-8 -*-
from openprocurement.contracting.api.utils import (
    contractingresource,
)
from openprocurement.contracting.api.views.document import (
    ContractsDocumentResource as BaseContractsDocumentResource,
)


@contractingresource(name='Contract Documents',
                     collection_path='/contracts/{contract_id}/documents',
                     path='/contracts/{contract_id}/documents/{document_id}',
                     description="Contract related binary files (PDFs, etc.)")
class ContractsDocumentResource(BaseContractsDocumentResource):
    """ ESCO Contract Docuemnt Resource """