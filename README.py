import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ExcelToArrayOfObjects {
    public static void main(String[] args) {
        String excelFilePath = "data.xlsx";  // Replace with your Excel file path

        List<Map<String, Object>> result = new ArrayList<>();

        try (FileInputStream fis = new FileInputStream(excelFilePath);
             Workbook workbook = new XSSFWorkbook(fis)) {

            Sheet sheet = workbook.getSheetAt(0);
            Row headerRow = sheet.getRow(0);
            int numberOfColumns = headerRow.getLastCellNum();

            for (int colIndex = 1; colIndex < numberOfColumns; colIndex++) {
                Map<String, Object> obj = new HashMap<>();
                
                // Loop through each row in the current column
                for (int rowIndex = 1; rowIndex <= sheet.getLastRowNum(); rowIndex++) {
                    Row row = sheet.getRow(rowIndex);
                    if (row != null) {
                        Cell keyCell = row.getCell(0);  // Key from the first column
                        Cell valueCell = row.getCell(colIndex);  // Value from the current column

                        if (keyCell != null && valueCell != null) {
                            String key = keyCell.getStringCellValue();
                            Object value = getCellValue(valueCell);
                            obj.put(key, value);
                        }
                    }
                }
                result.add(obj);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

        // Print the result
        for (Map<String, Object> map : result) {
            System.out.println(map);
        }
    }

    // Helper method to get the cell value as an Object
    private static Object getCellValue(Cell cell) {
        switch (cell.getCellType()) {
            case STRING:
                return cell.getStringCellValue();
            case NUMERIC:
                if (DateUtil.isCellDateFormatted(cell)) {
                    return cell.getDateCellValue();
                } else {
                    return cell.getNumericCellValue();
                }
            case BOOLEAN:
                return cell.getBooleanCellValue();
            case FORMULA:
                return cell.getCellFormula();
            case BLANK:
                return "";
            default:
                return null;
        }
    }
}
