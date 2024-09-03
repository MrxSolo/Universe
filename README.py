import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ProductDetailSplitter {
    public static void main(String[] args) {
        // First object (template)
        Map<String, Object> templateObject = new HashMap<>();
        templateObject.put("pOrderNo", 1);
        templateObject.put("pDetailName", "150ml");
        templateObject.put("pSize", "hello");

        // Second object (source for replacement and splitting)
        Map<String, Object> sourceObject = new HashMap<>();
        sourceObject.put("Product details", "100ml\n150ml\n200ml");
        sourceObject.put("packet size", "hello");

        // Call the function to split and replace values
        List<Map<String, Object>> result = splitAndReplaceValues(templateObject, sourceObject);

        // Print the result
        for (Map<String, Object> obj : result) {
            System.out.println(obj);
        }
    }

    /**
     * Splits product details from the source object and replaces values in the
     * template object to create a list of product objects.
     *
     * @param templateObject The template object containing initial key-value pairs.
     * @param sourceObject The source object with product details and other values.
     * @return A list of maps representing the new objects with replaced values.
     */
    public static List<Map<String, Object>> splitAndReplaceValues(Map<String, Object> templateObject, Map<String, Object> sourceObject) {
        // Extract product details and split by newline
        String productDetails = (String) sourceObject.get("Product details");
        String[] productArray = productDetails.split("\\n");

        // Extract packet size
        String packetSize = (String) sourceObject.get("packet size");

        // List to hold the resulting objects
        List<Map<String, Object>> result = new ArrayList<>();

        // Create new objects based on the number of products
        for (int i = 0; i < productArray.length; i++) {
            // Create a new map for each product
            Map<String, Object> newObj = new HashMap<>(templateObject);

            // Update values in the new object
            newObj.put("pOrderNo", i + 1);  // Order number starts from 1
            newObj.put("pDetailName", productArray[i]);  // Replace detail name
            newObj.put("pSize", packetSize);  // Replace size

            // Add the new object to the result list
            result.add(newObj);
        }

        return result;
    }
}
