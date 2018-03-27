# -*- coding: utf-8 -*-
from openprocurement.contracting.core.utils import contractingresource
from openprocurement.contracting.core.views.contract import (
    ContractResource as BaseContractResource,
)


@contractingresource(name='esco.EU:Contract',
                     path='/contracts/{contract_id}',
                     contractType='esco.EU',
                     description="Contract")
class ContractResource(BaseContractResource):
    """ ESCO Contract Resource """
