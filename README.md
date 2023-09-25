# CosmoClound_backend


---

# FastAPI E-commerce Application

Welcome to the FastAPI E-commerce Application! This application allows you to manage products and orders in an e-commerce system.

## Getting Started

Follow these steps to set up and run the FastAPI application on your local machine.

### Prerequisites

- Python 3.x installed on your system.
- MongoDB database set up and running.
- Postman or any API testing tool for making requests (optional).

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone git@github.com:divyanshu2003singh/CosmoClound_backend.git
   ```

2. Change into the project directory:

   ```bash
   cd ecommerce-app
   ```

3. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Open the `main.py` file and configure your MongoDB connection:

   ```python
   client = MongoClient("mongodb+srv://your_username:your_password@cluster_url")
   ```

   Replace `your_username`, `your_password`, and `cluster_url` with your MongoDB credentials and connection URL.

2. Configure your authentication token in the `controllers.py` file:

   ```python
   if token != "your_valid_token":
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
   ```

   Replace `"your_valid_token"` with your authentication token.

### Running the Application

1. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

   This will start the server, and you should see output indicating that the server is running.

2. Open your web browser or API testing tool and navigate to:

   ```
   http://localhost:8000/docs
   ```

   This will open the FastAPI interactive documentation where you can explore and test the available endpoints.

### Making Requests

You can use an API testing tool like Postman or tools like `curl` to make requests to the API. Here are some example requests:

- Create a product:

  ```http
  POST http://localhost:8000/createproducts
  Content-Type: application/json

  {
      "name": "Product Name",
      "price": 19.99,
      "available_quantity": 100
  }
  ```

- List products:

  ```http
  GET http://localhost:8000/products
  ```

- Create an order:

  ```http
  POST http://localhost:8000/orders
  Content-Type: application/json

  {
      "timestamp": "2023-09-25T14:30:00",
      "items": [
          {
              "productId": "123",
              "boughtQuantity": 2,
              "total_amount": 199.98
          },
          {
              "productId": "456",
              "boughtQuantity": 1,
              "total_amount": 49.99
          }
      ],
      "user_address": {
          "city": "Example City",
          "country": "Example Country",
          "zip_code": "12345"
      }
  }
  ```

### Additional Information

- This application includes basic error handling and logging. Any errors encountered during requests will be logged in the console.

- For production use, consider securing your MongoDB connection and using proper authentication mechanisms.

- The application is configured to use HTTP by default. If you want to use HTTPS, you need to set up SSL/TLS certificates and configure the server accordingly.

- This is a basic example application. You can extend it with more features and security measures for production use.

---

Feel free to customize this README file further to provide specific details about your application, such as authentication, authorization, and any other specific features you have implemented. Additionally, consider adding information about how to run the application in a production environment.
