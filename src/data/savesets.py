{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def save_sets(X_train=None, y_train=None, X_val=None, y_val=None, X_test=None, y_test=None, path='../data/processed/'):\n",
    "    \"\"\"Save the different sets locally\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    X_train: Numpy Array\n",
    "        Features for the training set\n",
    "    y_train: Numpy Array\n",
    "        Target for the training set\n",
    "    X_val: Numpy Array\n",
    "        Features for the validation set\n",
    "    y_val: Numpy Array\n",
    "        Target for the validation set\n",
    "    X_test: Numpy Array\n",
    "        Features for the testing set\n",
    "    y_test: Numpy Array\n",
    "        Target for the testing set\n",
    "    path : str\n",
    "        Path to the folder where the sets will be saved (default: '../data/processed/')\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    \"\"\"\n",
    "    import numpy as np\n",
    "\n",
    "    if X_train is not None:\n",
    "      np.save(f'{path}X_train', X_train)\n",
    "    if X_val is not None:\n",
    "      np.save(f'{path}X_val',   X_val)\n",
    "    if X_test is not None:\n",
    "      np.save(f'{path}X_test',  X_test)\n",
    "    if y_train is not None:\n",
    "      np.save(f'{path}y_train', y_train)\n",
    "    if y_val is not None:\n",
    "      np.save(f'{path}y_val',   y_val)\n",
    "    if y_test is not None:\n",
    "      np.save(f'{path}y_test',  y_test)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
