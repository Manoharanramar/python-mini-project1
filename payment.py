import qrcode

# Payment URL (You can change this if needed)
payment_url = "https://example-payment-gateway.com/pay?amount=150"

# Generate QR code
qr = qrcode.make(payment_url)

# Save the QR code image
qr.save("qr.png")

print("QR code generated and saved as 'qr.png'")
