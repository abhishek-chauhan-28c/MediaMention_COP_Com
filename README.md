# Media Mention Report Generator

This project is a Streamlit application designed to process and analyze media mentions from uploaded Excel files. The tool is particularly useful for generating insights about media mentions, identifying relevant influencers, and cleaning up unwanted data based on keyword-based and rule-based matching.

## Features

- **File Upload Functionality**: 
  - Upload two Excel files:
    1. Media mentions file.
    2. Keyword file containing sheets with include/exclude keywords, influencer lists, and more.

- **Multi-Sheet Handling**: 
  - Reads relevant sheets from the keyword file (e.g., unique `Y`, unique `N`, keywords, junk words, exclude lists, etc.).
  
- **Data Cleaning and Preprocessing**:
  - Removes unwanted "Resources" like Blogs or Forums.
  - Drops unnecessary columns while retaining essential fields.
  
- **Keyword and Junk Filtering**:
  - Identifies and filters records based on keywords, junk patterns, and exclude lists provided in the keyword file.

- **Mapping Influencers**:
  - Marks influencers found in specific sheets such as the "Sheet2".

- **New Columns for Analysis**:
  - Creates new computed columns such as `media mention`, `Combine`, `combine Text`, `Junk`, `Exclude`.

- **Interactive Data Display**:
  - Provides a clean preview of the processed data directly in the Streamlit app.

- **Improved User Interface**:
  - Custom branding with NetImpact Limited logo integrated at the top of the interface.

---

## Installation

To get started with the Media Mention Report Generator, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Abhi-pacific/MediaMention_COP_Com.git
   ```
2. Navigate to the project directory:
   ```bash
   cd MediaMention_COP_Com
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Ensure that `streamlit`, `pandas`, `openpyxl`, and other required libraries are installed.

4. Run the application:
   ```bash
   streamlit run MMstreamlitCode.py
   ```

---

## Usage

1. Launch the Streamlit app using the command above.
2. Upload the following files via the interface:
   - **Media mentions file** (Excel format, `.xlsx`).
   - **Keyword file** containing necessary sheets for processing (Excel format, `.xlsx`).
3. Click the **Process File** button to begin processing.
4. Review the processed data displayed in the application.

**Output Highlights:**
- Processed data will be shown in an interactive table.
- Columns include metadata like `Title`, `Text`, `Combine`, `URL`, `Author`, `Nickname`, `Potential reach`, and more.
- Filtered data based on media mentions (`Y`, `N`), junk removal, and keyword matches.

---

## Excel File Format Requirements

Ensure the uploaded Excel files are formatted as explained below:

- **Media mentions file**:
  - Should include columns like `Title`, `Text`, `URL`, `Author`, `Nickname`, `Profile`, `Subscribers`, `Source`, **`Resource type`**, and `Potential reach`.

- **Keyword and Rules File**:
  - Files should contain the following sheets:
    1. `Unique Y` (Influencers marked as Y)
    2. `Unique N` (Influencers marked as N)
    3. `Keywords` (Contains keywords to identify relevant rows)
    4. `Sheet2` (List for rule-based filtering)
    5. `Junkwords` (Contains terms to identify junk rows)
    6. `Exclude List` (Contains terms to exclude certain rows)

---

## Dependencies

- **Python Libraries**:
  - `pandas`
  - `re`
  - `streamlit`
  - `openpyxl`

---

## Example

### Input:
- **Media Mentions File:**
  - Contains data about media mentions, including text, URLs, and metadata.

- **Y/N Keyword File:**
  - Contains sheets outlining logic for filtering and categorizing data.

### Output:
- Cleaned dataframe preview displayed with meaningful columns.
- Insights such as:
  - Whether the mention is relevant, junk, or excluded.
  - Media mention classification as `Y`, `N`, or `Found in both`.
  - Matching keywords and junk patterns for better understanding.

---

## Key Functionality Walkthrough

1. **File Uploader**:
   - Prompts user to upload two Excel files.
   - Ensures both files are available before processing.

2. **Data Cleaning**:
   - Removes invalid `Resource type` values.
   - Drops unnecessary columns, presenting a streamlined dataset.

3. **Keyword Matching**:
   - Dynamically creates regex filters from provided keywords/junk terms/exclude lists.
   - Matches and categorizes data based on these filters.

4. **Output Display**:
   - Displays the cleaned dataset in the Streamlit interface, with new columns added for analysis.

---

## Logo Integration

The application has a branded UI, featuring the NetImpact Limited logo.

---

## Contribution Guidelines

We welcome contributions to this project. Feel free to fork the repository and submit pull requests! For significant changes, please open an issue first to discuss your proposed modifications.

---

## License

This project is open-source and distributed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code.

--- 

## Contact

If you have any questions, issues, or feedback, please raise an issue on the [GitHub repository](https://github.com/Abhi-pacific/MediaMention_COP_Com) or reach out to the author.

Happy coding!