""" Assignment 4: Unique Visitors Tracker
Write a program that keeps track of unique website visitors using a set. The program should allow adding new visitors and checking if a user has already visited.
Expected Output:
- Add a visitor
- Check if a visitor has already visited
- Display the total number of unique visitors
"""



class UniqueVisitorTracker:
    def __init__(self):
        self.visitors = set()  # Set to store unique visitors

    def add_visitor(self, visitor_id):
        if visitor_id in self.visitors:
            print(f"Visitor {visitor_id} has already visited.")
        else:
            self.visitors.add(visitor_id)
            print(f"Visitor {visitor_id} added.")

    def has_visited(self, visitor_id):
        return visitor_id in self.visitors

    def display_total_visitors(self):
        print(f"Total unique visitors: {len(self.visitors)}")

# Example usage
def main():
    tracker = UniqueVisitorTracker()
    tracker.add_visitor("user1")
    tracker.add_visitor("user2")
    tracker.add_visitor("user1")  # Duplicate entry
    print("Has user3 visited?", tracker.has_visited("user3"))
    tracker.display_total_visitors()

if __name__ == "__main__":
    main()