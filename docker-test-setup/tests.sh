# Build images
docker image build -t api-node api
docker image build -t database-node database
docker image build -t test-node test

# Create network
docker network create test-net

# Run database container
# echo "Running database container..."
docker container run --rm -d \
    --name postgres-container \
    --net test-net \
    database-node

# Wait 5 seconds
echo "Sleeping for 5 seconds..."
sleep 5

# Run api container
docker container run --rm -d \
    --name api-container \
    --net test-net \
    api-node

# Wait 5 seconds
echo "Sleeping for 5 seconds..."
sleep 5

# Run tests container
docker container run --rm -it \
    --name test-container \
    --net test-net \
    -e BASE_URL="http://api-container:5000" \
    test-node