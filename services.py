from web3 import HTTPProvider, Web3

import settings


def get_balance(address: str) -> int:
    w3 = Web3(HTTPProvider("https://polygon-rpc.com"))
    contract_address = Web3.to_checksum_address(settings.CONTRACT_ADDRESS)
    address = Web3.to_checksum_address(address)
    with open(settings.ABI_JSON_FILE, "r") as abi_file:
        contract = w3.eth.contract(contract_address, abi=abi_file.read())
        return contract.functions.balanceOf(address).call()


if __name__ == "__main__":
    get_balance("0x51f1774249Fc2B0C2603542Ac6184Ae1d048351d")
