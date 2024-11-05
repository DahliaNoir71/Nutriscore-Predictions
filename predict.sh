curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{
  "energy_100g": 300,
  "sugars_100g": 10,
  "fat_100g": 15,
  "proteins_100g": 8,
  "fiber_100g": 3,
  "salt_100g": 0.1
}'
