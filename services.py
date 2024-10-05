from web3 import HTTPProvider, Web3

import settings


class PolygonInfoService:
    def __init__(self, contract_address: str, abi: str, http_provider_url: str = "https://polygon-rpc.com"):
        self.w3 = Web3(HTTPProvider(http_provider_url))
        self.contract_address = Web3.to_checksum_address(contract_address)
        self.abi = abi

    def get_balance(self, address: str) -> int:
        address = Web3.to_checksum_address(address)
        contract = self.w3.eth.contract(self.contract_address, abi=self.abi)
        return contract.functions.balanceOf(address).call()

    def get_balance_batch(self, addresses: list[str]) -> list[int]:
        balances = []
        for address in addresses:
            balances.append(self.get_balance(address))
        return balances


if __name__ == "__main__":
    with open(settings.ABI_JSON_FILE, "r") as abi_json_file:
        service = PolygonInfoService(settings.CONTRACT_ADDRESS, abi_json_file.read())
        print(
            service.get_balance_batch(
                ["0x51f1774249Fc2B0C2603542Ac6184Ae1d048351d", "0x4830AF4aB9cd9E381602aE50f71AE481a7727f7C"]
            )
        )
