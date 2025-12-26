import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

# ==============================
# PATH CONFIGURATION 
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RAW_DATA_PATH = os.path.join(
    BASE_DIR,
    "..",
    "dataset_raw",        
    "AmesHousing.csv"     
)

OUTPUT_DIR = os.path.join(BASE_DIR, "ames_preprocessing")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ames_preprocessed.csv")

# ==============================
# MAIN FUNCTION
# ==============================
def main():
    print("===== AUTOMATED DATA PREPROCESSING STARTED =====")

    # ------------------------------
    # Load Dataset
    # ------------------------------
    print("\n[1] Loading dataset...")
    print("DEBUG PATH:", RAW_DATA_PATH)
    print("FILE ADA?", os.path.exists(RAW_DATA_PATH))

    df = pd.read_csv(RAW_DATA_PATH)
    print("Dataset loaded with shape:", df.shape)

    # ------------------------------
    # Handle Missing Values
    # ------------------------------
    print("\n[2] Handling missing values...")

    num_cols = df.select_dtypes(include=["int64", "float64"]).columns
    cat_cols = df.select_dtypes(include=["object"]).columns

    df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

    print("Missing values handled.")

    # ------------------------------
    # Remove Duplicates
    # ------------------------------
    print("\n[3] Removing duplicate rows...")
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    print(f"Rows before: {before}, after: {after}")

    # ------------------------------
    # Encoding Categorical Features
    # ------------------------------
    print("\n[4] Encoding categorical features...")
    df_encoded = pd.get_dummies(df, drop_first=True)
    print("Encoded dataset shape:", df_encoded.shape)

    # ------------------------------
    # Feature Scaling
    # ------------------------------
    print("\n[5] Scaling numerical features...")
    X = df_encoded.drop("SalePrice", axis=1)
    y = df_encoded["SalePrice"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # ------------------------------
    # Create Final Dataset
    # ------------------------------
    processed_df = pd.DataFrame(X_scaled, columns=X.columns)
    processed_df["SalePrice"] = y.values

    # ------------------------------
    # Save Output
    # ------------------------------
    print("\n[6] Saving preprocessed dataset...")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    processed_df.to_csv(OUTPUT_PATH, index=False)

    print("Preprocessing completed successfully!")
    print("Output saved to:", OUTPUT_PATH)


# ==============================
# ENTRY POINT
# ==============================
if __name__ == "__main__":
    main()