# YangTreeParser
This Python code processes a YANG file, extracts its tree structure using pyang, and saves the hierarchical paths to a text file.

This Python script processes a YANG file and extracts its tree structure using pyang. Here's a breakdown of its functionality:
- Running pyang to generate tree output:
- Specifies the path to the YANG file.
- Executes pyang to extract the tree structure from the YANG model.
- If pyang is missing or there are dependency issues, it prints relevant error messages.
- Parsing the pyang tree output and building hierarchical paths:
- Splits the tree output into individual lines.
- Processes each line to reconstruct the hierarchical YANG structure.
- Extracts the paths (similar to XPath) of YANG elements and stores them in a list.
- Saving extracted paths to paths.txt:
- Writes each identified path into a text file.
- Defines the output file name and determines where to save the paths.
- Calls pyang and processes the output.
Purpose: This script helps analyze YANG models by extracting structured paths, which can be useful for managing network configurations with NETCONF and YANG.

this script can be beneficial for telemetry systems, especially in model-driven telemetry (MDT) environments where structured data extraction is crucial. Since YANG models define network configurations and operational data, parsing them into hierarchical paths can assist in data collection, streaming, and visualization for telemetry purposes.


