{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a43331d8-67d8-41ff-a229-c758de244078",
   "metadata": {},
   "outputs": [],
   "source": [
    "import flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "36159504-56d7-4956-ab80-91c2963c6561",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask \n",
    "  \n",
    "app = Flask(__name__) \n",
        "app.run(debug=True, port=33507) \n",
    "@app.route(\"/\") \n",
    "def home_view(): \n",
    "        return \"<h1>Welcome to NS Facutly Database!</h1>\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78b625f8-96ea-41db-a6d7-9d6b63e76612",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
