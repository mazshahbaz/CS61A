test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> free_bacon(35)
          edcbd82ba98a8122be244fa325c62071
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> free_bacon(71)
          46caef5ffd6d72c8757279cbcf01b12f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> free_bacon(7)
          43d176e102c8d95338faf8791aa509b3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> free_bacon(17)
          46caef5ffd6d72c8757279cbcf01b12f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> free_bacon(0)
          43d176e102c8d95338faf8791aa509b3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> free_bacon(10)
          43d176e102c8d95338faf8791aa509b3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> free_bacon(70)
          43d176e102c8d95338faf8791aa509b3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> free_bacon(99)
          70e71b420a966665c548a3bb2cb30d7d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> free_bacon(57)
          327b19ffebddf93982e1ad2a4a6486f4
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
