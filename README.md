# CMPE 273-lab2 - A Simple Calculator Application using gRPC 

### Setting up the environment
```sh
# Ensure you have pip version 9.0.1 or higher:
$ python -m pip install --upgrade pip
# Install gRPC:
$ sudo python -m pip install grpcio
# To install gRPC tools, run:
$ python -m pip install grpcio-tools googleapis-common-protos
```

### Working with Protocol Buffer
  ~ gRPC service is defined using protocol buffers.
  ~ Create a service using the **_calculator.proto_** file.

### Generate gRPC code
```sh
$ python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto
```

### Create client and server
  ~ **_calculator_server.py_**. Implement the *addition* functionality.
  ~ **_calculator_client.py_**. Provide the parameters to *addition* function

### Running  gRPC Application
```sh
# Run the server
python3 calculator_server.py
# In another terminal, run the client
python3 calculator_client.py
```

### Congratulations! You’ve just run a client-server application with gRPC.