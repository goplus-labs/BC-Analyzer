import json
class BC_Analyzer:
    def __init__(self, bytecode: str):
        self.bytecode = bytecode

    def is_proxy(self) -> bool:
        DELEGATECALL = "f4"
        CALLCODE = "f2"
        EIP1967_SLOT = "eip1967.proxy.implementation"

        # Check for DELEGATECALL or CALLCODE opcodes
        if DELEGATECALL in self.bytecode or CALLCODE in self.bytecode:
            return True

        # Check for EIP-1967 recommended storage slot
        if EIP1967_SLOT in self.bytecode:
            return True

        # Check for known bytecode patterns
        known_patterns = ["PATTERN1", "PATTERN2"]
        if any(pattern in self.bytecode for pattern in known_patterns):
            return True

        return False

    def is_erc20(self) -> bool:
        ERC20_SELECTORS = ["18160ddd", "70a08231", "a9059cbb"]
        return all(selector in self.bytecode for selector in ERC20_SELECTORS)

    def is_erc721(self) -> bool:
        ERC721_SELECTORS = ["6352211e", "b88d4fde", "23b872dd"]
        return all(selector in self.bytecode for selector in ERC721_SELECTORS)

    def is_erc1155(self) -> bool:
        ERC1155_SELECTORS = ["d9b67a26", "a22cb465", "e985e9c5", "0e89341c"]  # Some of the core ERC1155 function selectors
        return all(selector in self.bytecode for selector in ERC1155_SELECTORS)

    def analyze(self) -> str:
        result = {
            "is_proxy": self.is_proxy(),
            "is_erc20": self.is_erc20(),
            "is_erc721": self.is_erc721(),
            "is_erc1155": self.is_erc1155()
        }
        return json.dumps(result, indent=4)