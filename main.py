# Simulated Backboard Assistant (for GHW submission)

import uuid

# Step 1: Create Assistant
assistant_id = "asst_" + str(uuid.uuid4())
print("Assistant created:", assistant_id)

# Step 2: Create Thread
thread_id = "thread_" + str(uuid.uuid4())
print("Thread created:", thread_id)

# Step 3: Send Message
user_message = "Say Hello World"

# Simulated AI response
response = "Hello World!"

print("User:", user_message)
print("Assistant:", response)