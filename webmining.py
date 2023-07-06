import requests
import tkinter as tk
import matplotlib.pyplot as plt

def get_data(state):
    url = "https://api.covid19india.org/data.json"
    response = requests.get(url)
    data = response.json()["statewise"]
    for d in data:
        if d["state"].lower() == state.lower():
            return int(d["confirmed"]), int(d["active"])
    return 0, 0

def show_graph(state1, state2, cases1, cases2, active1, active2):
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
    ax[0].bar(state1, cases1, width=0.4, label=state1)
    ax[0].bar(state2, cases2, width=0.4, label=state2)
    ax[0].set_xlabel("State")
    ax[0].set_ylabel("Confirmed Cases")
    ax[0].set_title("Confirmed Covid Cases Comparison")
    ax[0].legend()
    ax[1].bar(state1, active1, width=0.4, label=state1)
    ax[1].bar(state2, active2, width=0.4, label=state2)
    ax[1].set_xlabel("State")
    ax[1].set_ylabel("Active Cases")
    ax[1].set_title("Active Covid Cases Comparison")
    ax[1].legend()
    plt.show()

def compare_cases():
    state1 = entry_state1.get().strip()
    state2 = entry_state2.get().strip()
    cases1, active1 = get_data(state1)
    cases2, active2 = get_data(state2)
    show_graph(state1, state2, cases1, cases2, active1, active2)

# create the GUI
root = tk.Tk()
root.title("Covid Cases Comparison")

# create the entry and button widgets
entry_state1_label = tk.Label(root, text="Enter state 1:")
entry_state1_label.pack()
entry_state1 = tk.Entry(root)
entry_state1.pack()
entry_state2_label = tk.Label(root, text="Enter state 2:")
entry_state2_label.pack()
entry_state2 = tk.Entry(root)
entry_state2.pack()
button = tk.Button(root, text="Compare", command=compare_cases)
button.pack()

# start the GUI loop
root.mainloop()
