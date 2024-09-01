import java.util.HashMap;
import java.util.Map;

public class ReplaceValuesWithMappingDemo {
    public static void main(String[] args) {
        // Original object
        Map<String, Object> originalObject = new HashMap<>();
        originalObject.put("name", "John");
        originalObject.put("age", 25);
        originalObject.put("city", "Mumbai");
        originalObject.put("profession", "Engineer");

        // New object from the array
        Map<String, Object> newObject = new HashMap<>();
        newObject.put("p_name", "Alice");
        newObject.put("p_age", 30);
        newObject.put("city", "Delhi");

        // Define key mapping between original object and new object
        Map<String, String> keyMapping = new HashMap<>();
        keyMapping.put("name", "p_name");
        keyMapping.put("age", "p_age");
        keyMapping.put("city", "city");

        // Replace values based on the key mapping
        replaceValuesWithMapping(originalObject, newObject, keyMapping);

        // Print the modified original object
        System.out.println(originalObject);
    }

    /**
     * Replaces values in the original object with values from the new object
     * based on a provided key mapping.
     *
     * @param originalObject The original object whose values are to be replaced.
     * @param newObject The new object with the values to replace.
     * @param keyMapping A mapping of keys in the original object to keys in the new object.
     */
    public static void replaceValuesWithMapping(Map<String, Object> originalObject, Map<String, Object> newObject, Map<String, String> keyMapping) {
        // Loop through each entry in the key mapping
        for (Map.Entry<String, String> entry : keyMapping.entrySet()) {
            String originalKey = entry.getKey();
            String newKey = entry.getValue();

            // If the new object has the key mapped to the original key, replace the value
            if (newObject.containsKey(newKey)) {
                originalObject.put(originalKey, newObject.get(newKey));
            }
        }
    }
}
