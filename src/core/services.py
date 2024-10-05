from django.conf import settings
from moralis import evm_api
from web3 import HTTPProvider, Web3


class PolygonInfoService:
    def __init__(
        self,
        contract_address: str,
        abi_path: str = settings.ABI_JSON_FILE,
        http_provider_url: str = "https://polygon-rpc.com",
    ):
        self.w3 = Web3(HTTPProvider(http_provider_url))
        self.contract_address = Web3.to_checksum_address(contract_address)
        with open(abi_path, "r") as abi_json_file:
            self.abi = abi_json_file.read()

    def get_balance(self, address: str) -> int:
        address = Web3.to_checksum_address(address)
        contract = self.w3.eth.contract(self.contract_address, abi=self.abi)
        return contract.functions.balanceOf(address).call()

    def get_balance_batch(self, addresses: list[str]) -> list[int]:
        balances = []
        for address in addresses:
            balances.append(self.get_balance(address))
        return balances

    def get_top(self, n: int) -> list[tuple[str, int]]:
        params = {"chain": "polygon", "address": self.contract_address}

        result = evm_api.token.get_wallet_token_balances(
            api_key=settings.MORALIS_API_KEY,
            params=params,
        )

        result = sorted(result, key=lambda x: int(x["balance"]), reverse=True)[:n]
        return [(item["token_address"], item["balance"]) for item in result]

    def get_token_info(self, token_address: str) -> dict:
        params = {"chain": "polygon", "addresses": [token_address]}

        result = evm_api.token.get_token_metadata(
            api_key=settings.MORALIS_API_KEY,
            params=params,
        )

        return result[0]
