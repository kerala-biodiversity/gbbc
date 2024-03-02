# How to run the code.

- Create a `.env` file and add the API key there.

- Use required start date and end date by updating below lines from `data_update.py`.

```
start_date = date(2024,2,16) 
end_date = date(2024,2,19)
```

Then run the `data_update.py` code:

  ```
    python3 data_update.py
  ```

- Output will be updated in 2024 folder.

# Requirements

- requests
- python-dotenv
- pandas
  
