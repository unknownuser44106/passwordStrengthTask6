import csv
import passwordmeter

# Read passwords from a file
with open("passwords.txt", "r") as f:
    passwords = [line.strip() for line in f if line.strip()]

# Write results to CSV
with open("results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Sl No  ", "Password ", "Strength (%)"])
    
    for idx, pwd in enumerate(passwords, 1):
        strength, _ = passwordmeter.test(pwd)
        writer.writerow([idx, pwd, round(strength * 100, 2)])

print("Report saved as results.csv")
