{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def pop_target(df, target_col, to_numpy=False):\n",
    "    \"\"\"Extract target variable from dataframe and convert to nympy arrays if required\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    df : pd.DataFrame\n",
    "        Dataframe\n",
    "    target_col : str\n",
    "        Name of the target variable\n",
    "    to_numpy : bool\n",
    "        Flag stating to convert to numpy array or not\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    pd.DataFrame/Numpy array\n",
    "        Subsetted Pandas dataframe containing all features\n",
    "    pd.DataFrame/Numpy array\n",
    "        Subsetted Pandas dataframe containing the target\n",
    "    \"\"\"\n",
    "\n",
    "    df_copy = df.copy()\n",
    "    target = df_copy.pop(target_col)\n",
    "    \n",
    "    if to_numpy:\n",
    "        df_copy = df_copy.to_numpy()\n",
    "        target = target.to_numpy()\n",
    "    \n",
    "    return df_copy, target"
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
