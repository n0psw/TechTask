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
            print("Нет доступных фильмов.")
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

ю
def main():
    cinemaSystem = CinemaTicketSystem()

    while True:
        print("\nЗдравствуйте, у вас есть следующие доступные функции:")
        print("1. Добавить новый фильм")
        print("2. Показать все доступные фильмы")
        print("3. Добавить нового пользователя")
        print("4. Купить билет")
        print("5. Отменить покупку билета")
        print("6. Выйти")

        choice = input("Введите номер функции: ")

        if choice == '1':
            movieName = input("Введите название фильма: ")
            movieId = cinemaSystem.addMovie(movieName)
            print(f"Фильм добавлен с идентификатором: {movieId}")
        elif choice == '2':
            cinemaSystem.showAllMovies()
        elif choice == '3':
            userName = input("Введите имя пользователя: ")
            userId = cinemaSystem.addUser(userName)
            print(f"Пользователь добавлен с идентификатором: {userId}")
        elif choice == '4':
            userId = int(input("Введите идентификатор пользователя: "))
            movieId = int(input("Введите идентификатор фильма: "))
            ticketId = cinemaSystem.buyTicket(userId, movieId)
            if ticketId:
                print(f"Билет куплен с идентификатором: {ticketId}")
            else:
                print("Ошибка при покупке билета. Проверьте идентификаторы пользователя и фильма.")
        elif choice == '5':
            ticketId = int(input("Введите идентификатор билета: "))
            success = cinemaSystem.cancelTicket(ticketId)
            if success:
                print("Билет успешно отменен.")
            else:
                print("Ошибка при отмене билета. Билет с таким идентификатором не найден.")
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
