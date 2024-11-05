# Запуск бд, миграций и наполнения таблиц:
```bash
$ sudo docker compose build && sudo docker compose up -d
$ sudo docker compose exec app python app.py init_db
```
# Запуск скриптов для каждого из заданий (где n - номер от 1 до 5)
```bash
$ sudo docker compose exec app python app.py query{n}
```

# Результаты выполнения запросов:
## 1
```
Год рождения: 1984, Количество игроков: 1, Количество золотых медалей: 1
Год рождения: 1986, Количество игроков: 4, Количество золотых медалей: 5
Год рождения: 1991, Количество игроков: 3, Количество золотых медалей: 3
Год рождения: 1992, Количество игроков: 1, Количество золотых медалей: 1
Год рождения: 1993, Количество игроков: 1, Количество золотых медалей: 1
Год рождения: 1995, Количество игроков: 1, Количество золотых медалей: 1
Год рождения: 1996, Количество игроков: 2, Количество золотых медалей: 2
Год рождения: 1997, Количество игроков: 1, Количество золотых медалей: 1
Год рождения: 2000, Количество игроков: 1, Количество золотых медалей: 1
Год рождения: 2001, Количество игроков: 2, Количество золотых медалей: 2
Год рождения: 2003, Количество игроков: 1, Количество золотых медалей: 1
Год рождения: 2005, Количество игроков: 1, Количество золотых медалей: 2
Год рождения: 2006, Количество игроков: 3, Количество золотых медалей: 3
```

## 2
```
Событие: Recent Until, Количество золотых медалистов: 2, Результат: 14.339622030879616
Событие: Lose For, Количество золотых медалистов: 2, Результат: 11.025882511102575
Событие: Age Military, Количество золотых медалистов: 2, Результат: 10.146590947459728
Событие: Production Lot, Количество золотых медалистов: 2, Результат: 14.633413105527463
Событие: Job Usually, Количество золотых медалистов: 2, Результат: 13.626217256299604
Событие: Former Sea, Количество золотых медалистов: 2, Результат: 11.579393058089455
Событие: Small Issue, Количество золотых медалистов: 2, Результат: 13.980998616820466
Событие: Operation Somebody, Количество золотых медалистов: 2, Результат: 12.390262384330867
Событие: Clear Cost, Количество золотых медалистов: 2, Результат: 11.444284341432638
Событие: Generation East, Количество золотых медалистов: 2, Результат: 11.894809197701619
Событие: Painting Notice, Количество золотых медалистов: 2, Результат: 14.655475945033027
Событие: Entire Grow, Количество золотых медалистов: 2, Результат: 13.829981191435685
Событие: Sense Score, Количество золотых медалистов: 2, Результат: 11.020983842522433
Событие: Analysis Other, Количество золотых медалистов: 2, Результат: 11.423012854585394
Событие: Environmental Meet, Количество золотых медалистов: 2, Результат: 10.544730641245057
Событие: World Old, Количество золотых медалистов: 2, Результат: 11.787156513471647
Событие: Not Protect, Количество золотых медалистов: 2, Результат: 13.641657562821283
Событие: Night Summer, Количество золотых медалистов: 2, Результат: 10.860631433276394
Событие: Discussion Career, Количество золотых медалистов: 2, Результат: 9.727861747152652
Событие: Process Work, Количество золотых медалистов: 2, Результат: 9.891806354573049
```

## 3
```
Игрок: Anna Larsen, Олимпиада ID: O2000
Игрок: Anna Larsen, Олимпиада ID: O2008
Игрок: Anthony Little, Олимпиада ID: O2000
Игрок: Anthony Little, Олимпиада ID: O2004
Игрок: Anthony Little, Олимпиада ID: O2016
Игрок: Austin Boyer, Олимпиада ID: O2000
Игрок: Austin Boyer, Олимпиада ID: O2008
Игрок: Austin Boyer, Олимпиада ID: O2020
Игрок: Bianca Smith, Олимпиада ID: O2000
Игрок: Bianca Smith, Олимпиада ID: O2004
Игрок: Bianca Smith, Олимпиада ID: O2008
Игрок: Bradley Melton, Олимпиада ID: O2000
Игрок: Bradley Melton, Олимпиада ID: O2016
Игрок: Brandi Nguyen, Олимпиада ID: O2008
Игрок: Brandi Nguyen, Олимпиада ID: O2012
Игрок: Brandi Nguyen, Олимпиада ID: O2016
Игрок: Brandi Nguyen, Олимпиада ID: O2020
Игрок: Bryan Holt, Олимпиада ID: O2012
Игрок: Bryan Holt, Олимпиада ID: O2016
Игрок: Caleb Clark, Олимпиада ID: O2000
Игрок: Caleb Clark, Олимпиада ID: O2004
Игрок: Caleb Clark, Олимпиада ID: O2008
Игрок: Calvin Cook, Олимпиада ID: O2004
Игрок: Calvin Cook, Олимпиада ID: O2008
Игрок: Calvin Cook, Олимпиада ID: O2012
Игрок: Chad Mills, Олимпиада ID: O2000
Игрок: Chad Mills, Олимпиада ID: O2004
Игрок: Chad Mills, Олимпиада ID: O2008
Игрок: Charles Martinez, Олимпиада ID: O2000
Игрок: Charles Martinez, Олимпиада ID: O2008
Игрок: Charles Martinez, Олимпиада ID: O2016
Игрок: Charles Martinez, Олимпиада ID: O2020
Игрок: Cheryl Hamilton, Олимпиада ID: O2008
Игрок: Cheryl Hamilton, Олимпиада ID: O2016
Игрок: Cheryl Hamilton, Олимпиада ID: O2020
Игрок: Christopher Holden, Олимпиада ID: O2000
Игрок: Christopher Holden, Олимпиада ID: O2012
Игрок: Christopher Holden, Олимпиада ID: O2016
Игрок: Christopher York, Олимпиада ID: O2000
Игрок: Christopher York, Олимпиада ID: O2008
Игрок: Christopher York, Олимпиада ID: O2012
Игрок: Christopher York, Олимпиада ID: O2020
Игрок: Claudia Burns, Олимпиада ID: O2000
Игрок: Claudia Burns, Олимпиада ID: O2004
Игрок: Claudia Burns, Олимпиада ID: O2020
Игрок: Claudia Miller, Олимпиада ID: O2008
Игрок: Claudia Miller, Олимпиада ID: O2012
Игрок: Crystal Gill, Олимпиада ID: O2000
Игрок: Crystal Gill, Олимпиада ID: O2008
Игрок: Crystal Gill, Олимпиада ID: O2020
Игрок: David Fox, Олимпиада ID: O2000
Игрок: David Fox, Олимпиада ID: O2004
Игрок: David Fox, Олимпиада ID: O2020
Игрок: David Walker, Олимпиада ID: O2008
Игрок: David Walker, Олимпиада ID: O2012
Игрок: David Williams, Олимпиада ID: O2000
Игрок: David Williams, Олимпиада ID: O2008
Игрок: David Williams, Олимпиада ID: O2012
Игрок: David Williams, Олимпиада ID: O2016
Игрок: Dawn Jones, Олимпиада ID: O2000
Игрок: Dawn Jones, Олимпиада ID: O2008
Игрок: Dawn Jones, Олимпиада ID: O2012
Игрок: Dawn Jones, Олимпиада ID: O2016
Игрок: Deanna Johnson, Олимпиада ID: O2000
Игрок: Deanna Johnson, Олимпиада ID: O2004
Игрок: Deanna Johnson, Олимпиада ID: O2008
Игрок: Deanna Johnson, Олимпиада ID: O2016
Игрок: Deanna Johnson, Олимпиада ID: O2020
Игрок: Devon Morgan, Олимпиада ID: O2000
Игрок: Devon Morgan, Олимпиада ID: O2008
Игрок: Devon Morgan, Олимпиада ID: O2016
Игрок: Diana Good, Олимпиада ID: O2000
Игрок: Diana Good, Олимпиада ID: O2016
Игрок: Diana Good, Олимпиада ID: O2020
Игрок: Edwin Butler, Олимпиада ID: O2000
Игрок: Edwin Butler, Олимпиада ID: O2016
Игрок: Elizabeth Lynch, Олимпиада ID: O2000
Игрок: Elizabeth Lynch, Олимпиада ID: O2004
Игрок: Elizabeth Lynch, Олимпиада ID: O2012
Игрок: Erica Harris, Олимпиада ID: O2000
Игрок: Erica Harris, Олимпиада ID: O2004
Игрок: Erica Harris, Олимпиада ID: O2008
Игрок: Erica Harris, Олимпиада ID: O2012
Игрок: Felicia Cross, Олимпиада ID: O2000
Игрок: Felicia Cross, Олимпиада ID: O2016
Игрок: George Williams, Олимпиада ID: O2000
Игрок: George Williams, Олимпиада ID: O2012
Игрок: George Williams, Олимпиада ID: O2016
Игрок: Gerald Moreno, Олимпиада ID: O2000
Игрок: Gerald Moreno, Олимпиада ID: O2004
Игрок: Gerald Moreno, Олимпиада ID: O2020
Игрок: Gregory Lucero, Олимпиада ID: O2000
Игрок: Gregory Lucero, Олимпиада ID: O2004
Игрок: Gregory Lucero, Олимпиада ID: O2008
Игрок: Gregory Lucero, Олимпиада ID: O2016
Игрок: Heather Roberts, Олимпиада ID: O2008
Игрок: Heather Roberts, Олимпиада ID: O2016
Игрок: Isaiah Wilcox, Олимпиада ID: O2004
Игрок: Isaiah Wilcox, Олимпиада ID: O2008
Игрок: Isaiah Wilcox, Олимпиада ID: O2012
Игрок: Jaime Villegas, Олимпиада ID: O2000
Игрок: Jaime Villegas, Олимпиада ID: O2012
Игрок: Jaime Villegas, Олимпиада ID: O2016
Игрок: Jaime Villegas, Олимпиада ID: O2020
Игрок: James Clark, Олимпиада ID: O2000
Игрок: James Clark, Олимпиада ID: O2004
Игрок: James Clark, Олимпиада ID: O2012
Игрок: James Clark, Олимпиада ID: O2020
Игрок: James Garcia, Олимпиада ID: O2000
Игрок: James Garcia, Олимпиада ID: O2012
Игрок: James Garcia, Олимпиада ID: O2016
Игрок: James Garcia, Олимпиада ID: O2020
Игрок: Jane Garza, Олимпиада ID: O2000
Игрок: Jane Garza, Олимпиада ID: O2012
Игрок: Jane Garza, Олимпиада ID: O2016
Игрок: Jason Curtis, Олимпиада ID: O2000
Игрок: Jason Curtis, Олимпиада ID: O2004
Игрок: Jason Curtis, Олимпиада ID: O2012
Игрок: Jason Curtis, Олимпиада ID: O2016
Игрок: Jason Garcia, Олимпиада ID: O2000
Игрок: Jason Garcia, Олимпиада ID: O2004
Игрок: Jason Garcia, Олимпиада ID: O2016
Игрок: Jason Williams, Олимпиада ID: O2016
Игрок: Jeanne Wood, Олимпиада ID: O2008
Игрок: Jeanne Wood, Олимпиада ID: O2016
Игрок: Jeffery Brown, Олимпиада ID: O2000
Игрок: Jeffery Fischer, Олимпиада ID: O2016
Игрок: Jerome Page, Олимпиада ID: O2000
Игрок: Jerome Page, Олимпиада ID: O2004
Игрок: Jerome Page, Олимпиада ID: O2012
Игрок: Jerome Page, Олимпиада ID: O2016
Игрок: Jessica West, Олимпиада ID: O2000
Игрок: Jessica West, Олимпиада ID: O2004
Игрок: Jessica West, Олимпиада ID: O2016
Игрок: Joan Atkins, Олимпиада ID: O2000
Игрок: Joan Atkins, Олимпиада ID: O2004
Игрок: Joan Atkins, Олимпиада ID: O2008
Игрок: Joan Atkins, Олимпиада ID: O2012
Игрок: Joan Atkins, Олимпиада ID: O2016
Игрок: Joan Atkins, Олимпиада ID: O2020
Игрок: Jon Clay, Олимпиада ID: O2000
Игрок: Jon Clay, Олимпиада ID: O2004
Игрок: Jon Clay, Олимпиада ID: O2012
Игрок: Jon Clay, Олимпиада ID: O2020
Игрок: Joseph Jones, Олимпиада ID: O2004
Игрок: Joseph Jones, Олимпиада ID: O2016
Игрок: Joseph Wilson, Олимпиада ID: O2000
Игрок: Joseph Wilson, Олимпиада ID: O2004
Игрок: Joseph Wilson, Олимпиада ID: O2008
Игрок: Joseph Wilson, Олимпиада ID: O2016
Игрок: Joseph Wilson, Олимпиада ID: O2020
Игрок: Judith Miller, Олимпиада ID: O2000
Игрок: Judith Miller, Олимпиада ID: O2008
Игрок: Judith Miller, Олимпиада ID: O2016
Игрок: Judith Miller, Олимпиада ID: O2020
Игрок: Judy Graham, Олимпиада ID: O2000
Игрок: Judy Graham, Олимпиада ID: O2004
Игрок: Judy Graham, Олимпиада ID: O2008
Игрок: Judy Graham, Олимпиада ID: O2012
Игрок: Judy Graham, Олимпиада ID: O2016
Игрок: Katelyn Hoffman, Олимпиада ID: O2000
Игрок: Katelyn Hoffman, Олимпиада ID: O2004
Игрок: Katelyn Hoffman, Олимпиада ID: O2012
Игрок: Katelyn Hoffman, Олимпиада ID: O2016
Игрок: Katherine Ibarra, Олимпиада ID: O2000
Игрок: Katherine Ibarra, Олимпиада ID: O2008
Игрок: Katherine Ibarra, Олимпиада ID: O2016
Игрок: Katherine Ibarra, Олимпиада ID: O2020
Игрок: Kathryn Berry, Олимпиада ID: O2000
Игрок: Kathryn Berry, Олимпиада ID: O2016
Игрок: Kathryn Berry, Олимпиада ID: O2020
Игрок: Kristen Murphy, Олимпиада ID: O2000
Игрок: Kristen Murphy, Олимпиада ID: O2004
Игрок: Kristen Murphy, Олимпиада ID: O2012
Игрок: Kristen Murphy, Олимпиада ID: O2020
Игрок: Kyle Cruz, Олимпиада ID: O2000
Игрок: Kyle Cruz, Олимпиада ID: O2004
Игрок: Kyle Cruz, Олимпиада ID: O2012
Игрок: Kyle Cruz, Олимпиада ID: O2016
Игрок: Kyle Cruz, Олимпиада ID: O2020
Игрок: Kyle Lyons, Олимпиада ID: O2012
Игрок: Kyle Lyons, Олимпиада ID: O2016
Игрок: Larry Moore, Олимпиада ID: O2000
Игрок: Larry Moore, Олимпиада ID: O2008
Игрок: Larry Moore, Олимпиада ID: O2012
Игрок: Larry Moore, Олимпиада ID: O2016
Игрок: Larry Moore, Олимпиада ID: O2020
Игрок: Laura Wolfe, Олимпиада ID: O2000
Игрок: Laura Wolfe, Олимпиада ID: O2004
Игрок: Laura Wolfe, Олимпиада ID: O2016
Игрок: Lindsey Moore, Олимпиада ID: O2000
Игрок: Lindsey Moore, Олимпиада ID: O2012
Игрок: Lindsey Moore, Олимпиада ID: O2016
Игрок: Lindsey Moore, Олимпиада ID: O2020
Игрок: Lisa Hall, Олимпиада ID: O2000
Игрок: Lisa Hall, Олимпиада ID: O2008
Игрок: Lisa Hall, Олимпиада ID: O2016
Игрок: Lisa Miller, Олимпиада ID: O2016
Игрок: Logan Hughes, Олимпиада ID: O2000
Игрок: Logan Hughes, Олимпиада ID: O2012
Игрок: Logan Hughes, Олимпиада ID: O2016
Игрок: Marc Key, Олимпиада ID: O2000
Игрок: Marc Key, Олимпиада ID: O2004
Игрок: Marc Key, Олимпиада ID: O2008
Игрок: Marc Key, Олимпиада ID: O2016
Игрок: Marc Key, Олимпиада ID: O2020
Игрок: Mariah Payne, Олимпиада ID: O2000
Игрок: Mariah Payne, Олимпиада ID: O2004
Игрок: Mariah Payne, Олимпиада ID: O2008
Игрок: Mariah Payne, Олимпиада ID: O2016
Игрок: Mark Walsh, Олимпиада ID: O2000
Игрок: Mark Walsh, Олимпиада ID: O2012
Игрок: Mark Walsh, Олимпиада ID: O2016
Игрок: Martin Anderson, Олимпиада ID: O2000
Игрок: Martin Anderson, Олимпиада ID: O2004
Игрок: Martin Anderson, Олимпиада ID: O2008
Игрок: Martin Anderson, Олимпиада ID: O2012
Игрок: Martin Anderson, Олимпиада ID: O2016
Игрок: Melody Haas, Олимпиада ID: O2012
Игрок: Melody Haas, Олимпиада ID: O2016
Игрок: Michael Cantu, Олимпиада ID: O2000
Игрок: Michael Cantu, Олимпиада ID: O2008
Игрок: Michael Cantu, Олимпиада ID: O2016
Игрок: Michael Simmons, Олимпиада ID: O2000
Игрок: Michael Simmons, Олимпиада ID: O2016
Игрок: Mr. Aaron Hale, Олимпиада ID: O2000
Игрок: Mr. Aaron Hale, Олимпиада ID: O2004
Игрок: Mr. Aaron Hale, Олимпиада ID: O2008
Игрок: Mr. Aaron Hale, Олимпиада ID: O2012
Игрок: Mr. Aaron Hale, Олимпиада ID: O2020
Игрок: Nicole Wise, Олимпиада ID: O2004
Игрок: Nicole Wise, Олимпиада ID: O2008
Игрок: Nicole Wise, Олимпиада ID: O2012
Игрок: Nicole Wise, Олимпиада ID: O2020
Игрок: Patricia Fletcher, Олимпиада ID: O2016
Игрок: Peggy Hale, Олимпиада ID: O2000
Игрок: Peggy Hale, Олимпиада ID: O2008
Игрок: Peggy Hale, Олимпиада ID: O2016
Игрок: Peggy Hale, Олимпиада ID: O2020
Игрок: Peter Gibson, Олимпиада ID: O2000
Игрок: Peter Gibson, Олимпиада ID: O2004
Игрок: Peter Gibson, Олимпиада ID: O2012
Игрок: Peter Gibson, Олимпиада ID: O2016
Игрок: Raven Jordan, Олимпиада ID: O2000
Игрок: Raven Jordan, Олимпиада ID: O2004
Игрок: Raven Jordan, Олимпиада ID: O2012
Игрок: Raven Jordan, Олимпиада ID: O2016
Игрок: Raven Jordan, Олимпиада ID: O2020
Игрок: Rebecca Wilson, Олимпиада ID: O2000
Игрок: Rebecca Wilson, Олимпиада ID: O2004
Игрок: Rebecca Wilson, Олимпиада ID: O2012
Игрок: Rebecca Wilson, Олимпиада ID: O2016
Игрок: Rebecca Wilson, Олимпиада ID: O2020
Игрок: Regina West, Олимпиада ID: O2000
Игрок: Regina West, Олимпиада ID: O2004
Игрок: Regina West, Олимпиада ID: O2008
Игрок: Richard Becker, Олимпиада ID: O2004
Игрок: Richard Becker, Олимпиада ID: O2012
Игрок: Richard Becker, Олимпиада ID: O2016
Игрок: Richard Becker, Олимпиада ID: O2020
Игрок: Robert Golden, Олимпиада ID: O2000
Игрок: Robert Golden, Олимпиада ID: O2008
Игрок: Robert Golden, Олимпиада ID: O2016
Игрок: Robert Golden, Олимпиада ID: O2020
Игрок: Sarah Jacobson, Олимпиада ID: O2000
Игрок: Sarah Jacobson, Олимпиада ID: O2004
Игрок: Sarah Jacobson, Олимпиада ID: O2008
Игрок: Sarah Sanchez, Олимпиада ID: O2004
Игрок: Sarah Sanchez, Олимпиада ID: O2012
Игрок: Sarah Sanchez, Олимпиада ID: O2020
Игрок: Sarah Villanueva, Олимпиада ID: O2000
Игрок: Sarah Villanueva, Олимпиада ID: O2004
Игрок: Sarah Villanueva, Олимпиада ID: O2012
Игрок: Sarah Villanueva, Олимпиада ID: O2016
Игрок: Seth Chambers, Олимпиада ID: O2008
Игрок: Seth Chambers, Олимпиада ID: O2012
Игрок: Seth Chambers, Олимпиада ID: O2020
Игрок: Shelly Lowery, Олимпиада ID: O2000
Игрок: Shelly Lowery, Олимпиада ID: O2004
Игрок: Shelly Lowery, Олимпиада ID: O2008
Игрок: Shelly Lowery, Олимпиада ID: O2016
Игрок: Shelly Lowery, Олимпиада ID: O2020
Игрок: Sherry Simpson, Олимпиада ID: O2000
Игрок: Sherry Simpson, Олимпиада ID: O2004
Игрок: Sherry Simpson, Олимпиада ID: O2008
Игрок: Sherry Simpson, Олимпиада ID: O2012
Игрок: Sherry Simpson, Олимпиада ID: O2016
Игрок: Steve Guzman, Олимпиада ID: O2000
Игрок: Steve Guzman, Олимпиада ID: O2012
Игрок: Steve Guzman, Олимпиада ID: O2016
Игрок: Steven Clark, Олимпиада ID: O2004
Игрок: Steven Clark, Олимпиада ID: O2012
Игрок: Sue Ramirez, Олимпиада ID: O2000
Игрок: Sue Ramirez, Олимпиада ID: O2016
Игрок: Tammy Walls, Олимпиада ID: O2004
Игрок: Tammy Walls, Олимпиада ID: O2012
Игрок: Tammy Walls, Олимпиада ID: O2016
Игрок: Tammy Walls, Олимпиада ID: O2020
Игрок: Tara Smith, Олимпиада ID: O2000
Игрок: Tara Smith, Олимпиада ID: O2004
Игрок: Tara Smith, Олимпиада ID: O2016
Игрок: Tara Smith, Олимпиада ID: O2020
Игрок: Taylor Guzman, Олимпиада ID: O2012
Игрок: Teresa Browning, Олимпиада ID: O2000
Игрок: Teresa Browning, Олимпиада ID: O2004
Игрок: Teresa Browning, Олимпиада ID: O2008
Игрок: Teresa Browning, Олимпиада ID: O2016
Игрок: Teresa Browning, Олимпиада ID: O2020
Игрок: Theresa Estrada, Олимпиада ID: O2000
Игрок: Theresa Estrada, Олимпиада ID: O2004
Игрок: Theresa Estrada, Олимпиада ID: O2016
Игрок: Tina Lucero, Олимпиада ID: O2000
Игрок: Tina Lucero, Олимпиада ID: O2004
Игрок: Tina Lucero, Олимпиада ID: O2008
Игрок: Tina Lucero, Олимпиада ID: O2012
Игрок: Tina Lucero, Олимпиада ID: O2020
Игрок: Todd Willis, Олимпиада ID: O2000
Игрок: Todd Willis, Олимпиада ID: O2004
Игрок: Todd Willis, Олимпиада ID: O2008
Игрок: Todd Willis, Олимпиада ID: O2012
Игрок: Tracy Reeves, Олимпиада ID: O2004
Игрок: Tracy Reeves, Олимпиада ID: O2008
Игрок: Tracy Reeves, Олимпиада ID: O2016
Игрок: Tracy Reeves, Олимпиада ID: O2020
Игрок: Tyler Peterson, Олимпиада ID: O2000
Игрок: Veronica Lowe, Олимпиада ID: O2016
Игрок: Veronica Lowe, Олимпиада ID: O2020
Игрок: William Green, Олимпиада ID: O2000
Игрок: William Green, Олимпиада ID: O2004
Игрок: William Green, Олимпиада ID: O2008
Игрок: William Green, Олимпиада ID: O2016
```

## 4
```
Страна: Senegal, Процент: 22.22%
```

## 5
```
Страна: Tanzania, Соотношение: 2.1452672878293342e-09
Страна: Bhutan, Соотношение: 3.965006640402801e-09
Страна: Armenia, Соотношение: 4.65445496607348e-09
Страна: Myanmar, Соотношение: 4.694479587209966e-09
Страна: Iraq, Соотношение: 6.730566796029442e-09
```

Результаты должны быть воспроизводимыми, так как у `faker` задан константный `seed`

# Какие скрипты где?
- `app/seed.py` - скрипт заполняющий таблицы
- `app/queries.py` - запросы для каждого задания
- `app/models.py` - модели для таблиц в описани __SQLAlchemy__ 
- `app/main.py` - точка входа, CLI
