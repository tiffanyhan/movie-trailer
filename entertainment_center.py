import fresh_tomatoes
import media

eternal_sunshine = media.Movie("Eternal Sunshine",
                               "When their relationship turns sour, a couple undergoes a procedure to have each other erased from their memories. But it is only through the process of loss that they discover what they had to begin with.",
                               "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",
                               "https://www.youtube.com/watch?v=rb9a00bXf-U")

#print(eternal_sunshine.storyline) 


john_malkovich = media.Movie("Being John Malkovich",
                             "A puppeteer discovers a portal that leads literally into the head of movie star John Malkovich.",
                             "https://upload.wikimedia.org/wikipedia/en/5/55/Being_John_Malkovich_poster.jpg",
                             "https://www.youtube.com/watch?v=2UuRFr0GnHM")

#print(john_malkovich.storyline)

#eternal_sunshine.show_trailer()

josie_pussycats = media.Movie("Josie and the Pussycats",
                              "A girl group find themselves in the middle of a conspiracy to deliver subliminal messages through popular music in this send up of the music industry and pop culture.",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Josie-pussycats-2001-movie.jpg/220px-Josie-pussycats-2001-movie.jpg",
                              "https://www.youtube.com/watch?v=LU5bOAyDbHc")

#josie_pussycats.show_trailer()

welcome_dollhouse = media.Movie("Welcome to the Dollhouse",
                                "An unattractive seventh grader struggles to cope with inattentive parents, snobbish classmates, a smart older brother, an attractive younger sister, and her own insecurities in suburban New Jersey.",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/WDollhouseMoviePoster.jpg/200px-WDollhouseMoviePoster.jpg",
                                "https://www.youtube.com/watch?v=JhXGDDN4PMI")

requiem_dream = media.Movie("Requiem for a Dream",
                            "The drug-induced utopias of four Coney Island people are shattered when their addictions run deep.",
                            "https://upload.wikimedia.org/wikipedia/en/9/92/Requiem_for_a_dream.jpg",
                            "https://www.youtube.com/watch?v=jzk-lmU4KZ4")

there_blood = media.Movie("There Will Be Blood",
                          "A story of family, religion, hatred, oil and madness, focusing on a turn-of-the-century prospector in the early days of the business.",
                          "https://upload.wikimedia.org/wikipedia/en/d/da/There_Will_Be_Blood_Poster.jpg",
                          "https://www.youtube.com/watch?v=FeSLPELpMeM")

movies = [eternal_sunshine, john_malkovich, josie_pussycats, welcome_dollhouse, requiem_dream, there_blood]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__module__)
