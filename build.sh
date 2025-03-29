docker build -t $JOB_NAME:$BUILD_ID .

docker tag $JOB_NAME:$BUILD_ID vishal161205/$JOB_NAME:$BUILD_ID

docker tag $JOB_NAME:$BUILD_ID vishal161205/$JOB_NAME:latest

docker push vishal161205/$JOB_NAME:$BUILD_ID

docker push vishal161205/$JOB_NAME:latest

docker rmi -f $JOB_NAME:$BUILD_ID vishal161205/$JOB_NAME:$BUILD_ID jacksneel/$JOB_NAME:latest
