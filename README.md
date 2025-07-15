# 🧊 Smart Cold Chain Risk Calculator

![App Screenshot](app_screenshot.png)

A Digital Health Solution to safeguard temperature-sensitive health shipments across global cold chain networks.

## 🔍 Overview

The **Smart Cold Chain Risk Calculator** is a decision-support tool built to assess the risk of spoilage, delay, or loss for biologics, vaccines, lab specimens, and other cold chain-dependent materials. It helps logistics professionals, researchers, and public health teams make data-informed shipping decisions — reducing waste, enhancing efficiency, and protecting patient outcomes.

## 💡 Key Features

- 📦 **Interactive Input Form** — Enter shipment details like product type, temperature range, origin, destination, packaging, and carrier.
- 📊 **Real-Time Risk Scores** — Calculates risk levels for:
  - Temperature deviation
  - Transit time and delays
  - Regional and seasonal risk
- 🛠 **Actionable Recommendations** — Auto-generated insights for improving cold chain reliability.
- 📈 **Simple, Executive-Friendly UI** — Powered by Streamlit for speed and simplicity.

## 🚚 Use Cases

- National vaccine distribution
- Clinical trial sample transport
- Lab-to-lab specimen transfers
- Remote region healthcare logistics
- NGO and global health shipment planning

## 🔧 Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **Language**: Python 3.10+
- **Deployment**: Ready for [Render](https://render.com), Streamlit Cloud, or local environments

## 🚀 Deployment (Render)

1. Fork or clone this repository.
2. Ensure you have a `requirements.txt` with:
    ```
    streamlit
    ```
3. Optional `render.yaml` for Render setup:
    ```yaml
    services:
      - type: web
        name: cold-chain-risk-calculator
        env: python
        buildCommand: ""
        startCommand: streamlit run cold_chain_risk_calculator.py --server.port=10000
        plan: free
    ```
4. Push to GitHub and connect your repo on [Render.com](https://render.com).

## 📁 Project Structure

cold-chain-risk-calc/
├── cold_chain_risk_calculator.py # Main app file
├── requirements.txt # Dependencies
├── render.yaml # Optional Render config
└── README.md # Project overview

yaml
Copy
Edit

## 📣 About the Creator

**Tobi Ogunbowale**  
Digital Health Project Manager | Lab Informatics & Workflow Optimization  
🌐 [tobiogunbowale.com](https://tobiogunbowale.com)  
🧠 Building AI for Cold Chain & HealthOps Transformation  

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change or add.

## 🛡 License

This project is open-source and available under the [MIT License](LICENSE).

---

> **“We don’t just move samples. We protect lives in transit.”**
