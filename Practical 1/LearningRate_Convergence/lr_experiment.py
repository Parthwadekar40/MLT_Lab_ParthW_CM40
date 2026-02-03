import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import log_loss

# 1. Load dataset
X, y = load_iris(return_X_y=True)
X = X[y != 2]
y = y[y != 2]

# 2. Split and Scale
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3. Parameters
learning_rates = [0.0001, 0.001, 0.01, 0.1]
epochs = 50

plt.figure(figsize=(8, 5))

# 4. Training Loop
for lr in learning_rates:
    model = SGDClassifier(
        loss="log_loss",
        learning_rate="constant",
        eta0=lr,
        max_iter=1,
        warm_start=True,
        random_state=42
    )

    losses = []
    for epoch in range(epochs):
        model.fit(X_train, y_train)
        y_prob = model.predict_proba(X_train)
        losses.append(log_loss(y_train, y_prob))

    # This print MUST be indented inside the 'lr' loop
    print(f"LR: {lr} | Final Loss: {losses[-1]:.4f}")
    plt.plot(losses, label=f"LR = {lr}")

plt.xlabel("Epochs")
plt.ylabel("Log Loss")
plt.title("Convergence by Learning Rate")
plt.legend()
plt.show()