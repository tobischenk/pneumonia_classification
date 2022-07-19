# pneumonia_classification

## Starting the fastapi server
The Server can be started either in a docker-compose network or on your localhost.

To start on the localhost, run `make runserver` in the project root directory.
You can stop the server with ctrl+c at any time.

To start a docker-compose running using the Dockerfile, run 

`make dc-up`

To inspect logs of the fastapi container, run 

`make dc-logs`

To stop the docker-compose network run 

`make dc-down`.

The server will in both cases be listening to port 8000 on your localhost.
Therefore, you can not run both the local server and the docker-compose network at the same time.

## Network Training
The Network was trained using google colab using the provided notebook in the notebooks folder.
The Data has to be uploaded to your personal drive folder and you have to adjust the file paths to recreate.

## Quality
The Network achieved an Accuracy of 0.8958333333333334 with a Recall of 0.9743589743589743.
It used class_weights to combat the existing class imbalance.

The Confusion Matrix for the Test Data is as follows:
![image info](./images/cm.png)

## Improvements
Instead of using class_weights, data augmentation to balance the dataset could help to further improve accuracy and recall.
Also tuning the hyperparameter using e.g. hyperas could potentionally improve the quality of the results.

Moreover, other architectures could create better results, but were not tested yet.