import dataclasses

from backend.objects.Section import Section


def main():
    sub1 = Section(status=' ', name='MATH 100 A11', activity='Discussion',
                   term=1, mode='In-Person', times={'Mon': (1100, 1200)})
    sub2 = Section(status=' ', name='MATH 100 A12', activity='Discussion',
                   term=1, mode='In-Person', times={'Wed': (900, 1000)})

    s = Section(status=' ', name='MATH 100 1A1', activity='Lecture',
                term=1, mode='In-Person', times={'Tue': (800, 1000)},
                dependencies=[sub1, sub2])
    print(dataclasses.asdict(s))


if __name__ == '__main__':
    main()
