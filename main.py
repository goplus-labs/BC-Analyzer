import json
from bc_analyzer import BC_Analyzer

if __name__ == "__main__":
    bytecode_input = input("Enter the contract bytecode: ")
    analyzer = BC_Analyzer(bytecode_input)
    print(analyzer.analyze())
