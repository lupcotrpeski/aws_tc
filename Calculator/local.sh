# Set the credentials
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
# Start the x-ray service
docker run --attach STDOUT -v ~/.aws/:/root/.aws/:ro --net=host -e AWS_REGION=ap-southeast-2 --name xray-daemon -p 2000:2000/udp --rm xray -o
docker run --attach STDOUT --net=host -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_REGION=ap-southeast-2 --name xray-daemon -p 2000:2000/udp --rm xray -o

# Start the freefood service
docker run -it -e API_GATEWAY=https://lmgr6g5bgf.execute-api.ap-southeast-2.amazonaws.com -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION=ap-southeast-2 -e ENVIRONMENT=dev -p80:80 --name freefood --rm ltrpeski/freefood:0.10