{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def split_sets_random(df, target_col, test_ratio=0.2, to_numpy=False):\n",
    "    \"\"\"Split sets randomly\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    df : pd.DataFrame\n",
    "        Input dataframe\n",
    "    target_col : str\n",
    "        Name of the target column\n",
    "    test_ratio : float\n",
    "        Ratio used for the validation and testing sets (default: 0.2)\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    Numpy Array\n",
    "        Features for the training set\n",
    "    Numpy Array\n",
    "        Target for the training set\n",
    "    Numpy Array\n",
    "        Features for the validation set\n",
    "    Numpy Array\n",
    "        Target for the validation set\n",
    "    Numpy Array\n",
    "        Features for the testing set\n",
    "    Numpy Array\n",
    "        Target for the testing set\n",
    "    \"\"\"\n",
    "    \n",
    "    from sklearn.model_selection import train_test_split\n",
    "    \n",
    "    features, target = pop_target(df=df, target_col=target_col, to_numpy=to_numpy)\n",
    "    \n",
    "    X_data, X_test, y_data, y_test = train_test_split(features, target, test_size=test_ratio, random_state=8)\n",
    "    \n",
    "    val_ratio = test_ratio / (1 - test_ratio)\n",
    "    X_train, X_val, y_train, y_val = train_test_split(X_data, y_data, test_size=val_ratio, random_state=8)\n",
    "\n",
    "    return X_train, y_train, X_val, y_val, X_test, y_test"
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
