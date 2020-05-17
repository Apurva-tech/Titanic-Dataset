{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_data(data):\n",
    "    data[\"Fare\"] = data[\"Fare\"].fillna(data[\"Fare\"].dropna().median())\n",
    "    data[\"Age\"] = data[\"Age\"].fillna(data[\"Age\"].dropna().median())\n",
    "    \n",
    "    data.loc[data[\"Sex\"]==\"male\",\"Sex\"]=0\n",
    "    data.loc[data[\"Sex\"]==\"female\",\"Sex\"]=1\n",
    "    \n",
    "    data[\"Embarked\"]=data[\"Embarked\"].fillna(\"S\")\n",
    "    data.iloc[data[\"Embarked\"] == 'S' ,\"Embarked\"]=0\n",
    "    data.iloc[data[\"Embarked\"] == 'S' ,\"Embarked\"]=1\n",
    "    data.iloc[data[\"Embarked\"] == 'S' ,\"Embarked\"]=2"
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
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
