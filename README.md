# BC_Analyzer

BC_Analyzer is a Python-based tool designed to analyze Ethereum contract bytecode. It determines whether a contract is a proxy contract and identifies if it adheres to popular token standards like ERC-20, ERC-721, and ERC-1155.

## Features

- Detects if a contract is a proxy contract.
- Identifies if a contract is of type ERC-20, ERC-721, or ERC-1155.
- Outputs results in a structured JSON format.

## Requirements

- Python 3.x

## Usage

1. Clone the repository:
   ```bash
   git clone [repository_url]
   cd BC_Analyzer
   ```

2. Run the script:
   ```bash
   python bc_analyzer.py
   ```

3. Enter the contract bytecode when prompted.

4. View the analysis results in JSON format.

## Output Format

The output is a JSON object with the following fields:

- `is_proxy`: A boolean indicating if the contract is a proxy contract.
- `is_erc20`: A boolean indicating if the contract adheres to the ERC-20 standard.
- `is_erc721`: A boolean indicating if the contract adheres to the ERC-721 standard.
- `is_erc1155`: A boolean indicating if the contract adheres to the ERC-1155 standard.

Example:

```json
{
    "is_proxy": true,
    "is_erc20": false,
    "is_erc721": false,
    "is_erc1155": true
}
```

## Limitations

- The tool provides a basic analysis based on known patterns in the bytecode. It might not detect custom or less-known proxy implementations.
- The presence of function selectors in the bytecode does not guarantee full compliance with a standard. A comprehensive code audit is recommended for complete assurance.

## Contributions

Contributions are welcome! Please submit pull requests or open issues to improve the tool or add new features.

## License

[MIT License](LICENSE)

---

Feel free to modify and expand upon this README to better fit the specifics of your project and its setup.