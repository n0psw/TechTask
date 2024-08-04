class CinemaTicketSystem:
    def __init__(self):
        self.movies = {}
        self.users = {}
        self.tickets = {}
        self.next_movie_id = 1
        self.next_user_id = 1
        self.next_ticket_id = 1

    def addMovie(self, movieName):
        movie_id = self.next_movie_id
        self.movies[movie_id] = movieName
        self.next_movie_id += 1
        return movie_id

    def showAllMovies(self):
        if not self.movies:
            print("��� ��������� �������.")
        else:
            for movie_id, movie_name in self.movies.items():
                print(f"{movie_id}. {movie_name}")

    def addUser(self, userName):
        user_id = self.next_user_id
        self.users[user_id] = userName
        self.next_user_id += 1
        return user_id

    def buyTicket(self, userId, movieId):
        if userId in self.users and movieId in self.movies:
            ticket_id = self.next_ticket_id
            self.tickets[ticket_id] = (userId, movieId)
            self.next_ticket_id += 1
            return ticket_id
        return None

    def cancelTicket(self, ticketId):
        if ticketId in self.tickets:
            del self.tickets[ticketId]
            return True
        return False

�
def main():
    cinemaSystem = CinemaTicketSystem()

    while True:
        print("\n������������, � ��� ���� ��������� ��������� �������:")
        print("1. �������� ����� �����")
        print("2. �������� ��� ��������� ������")
        print("3. �������� ������ ������������")
        print("4. ������ �����")
        print("5. �������� ������� ������")
        print("6. �����")

        choice = input("������� ����� �������: ")

        if choice == '1':
            movieName = input("������� �������� ������: ")
            movieId = cinemaSystem.addMovie(movieName)
            print(f"����� �������� � ���������������: {movieId}")
        elif choice == '2':
            cinemaSystem.showAllMovies()
        elif choice == '3':
            userName = input("������� ��� ������������: ")
            userId = cinemaSystem.addUser(userName)
            print(f"������������ �������� � ���������������: {userId}")
        elif choice == '4':
            userId = int(input("������� ������������� ������������: "))
            movieId = int(input("������� ������������� ������: "))
            ticketId = cinemaSystem.buyTicket(userId, movieId)
            if ticketId:
                print(f"����� ������ � ���������������: {ticketId}")
            else:
                print("������ ��� ������� ������. ��������� �������������� ������������ � ������.")
        elif choice == '5':
            ticketId = int(input("������� ������������� ������: "))
            success = cinemaSystem.cancelTicket(ticketId)
            if success:
                print("����� ������� �������.")
            else:
                print("������ ��� ������ ������. ����� � ����� ��������������� �� ������.")
        elif choice == '6':
            break
        else:
            print("�������� �����. ���������� ��� ���.")

if __name__ == "__main__":
    main()
