import os
import json

base_url = "https://raw.githubusercontent.com/Sunless72/Equilibrium-Assets/main/Exercises/"
output_file = "metadata.json"
data = {"exercises": []}

# Walk through the directory
for root, dirs, files in os.walk("Exercises"):
    for file in files:
        if file.endswith(".mp4"):
            # Get category from the parent folder name
            category = os.path.basename(root)
            
            # Create a URL-friendly path
            relative_path = os.path.join(category, file).replace("\\", "/")
            url = base_url + relative_path.replace(" ", "%20")
            
            # Create entry
            entry = {
                "id": os.path.splitext(file)[0].lower().replace(" ", "_"),
                "name": os.path.splitext(file)[0],
                "category": category,
                "url": url
            }
            data["exercises"].append(entry)

# Save to JSON
with open(output_file, "w") as f:
    json.dump(data, f, indent=2)

print(f"Successfully generated {output_file} with {len(data['exercises'])} videos!")
