import zlib, base64
exec(zlib.decompress(base64.b64decode('eJzNWW1v2zYQ/u5foRkoLCWKK6XtMBjjsDVva5LFbeWsKTJDUG3aVidLqiQncQL/95GSrbuj6KQtNmAfHEi8Fx7v5bmj0m63D5J5uih4bhQzbvC7lI8KPjZuw9jIgoIbycRIYm7khXybLo1gGoRxXhhBnAiBrNtut1uf/kjufvv9z7+9EQs+5fD6muWLObzesOMgyjksfGRhLpUF8QitDtg8uIPXd6xYpBGixyzNwriAhYLNwxheD9jR3YinRZigxQuWBfEUtMxSFoU5KJl5rFimvDXJkrkxSqJIuEEoyI1wniZZYcTBnI8rQ8Z8YtR6uTmJrV6rXkg99rBqGYRnae7U5JlkNkKgpjNDeNIQ7gYVkgW9XgPvkE1iok1wZrxYZPEW/pZK9pb0ALlZc99L29bs7h4sU4FbEOjb9eOxlCV89+ZdeVZ1/5F598x19sy7589dxxKPVtPGe7SHxZhu/diiZn0G0ikJyCWIvzbBNafweD6cJBkInJNgnA6FfY/R5Rn1Wp8zMIIaewjGBnaSpqLC4sLPR0nGUQxe1tmZRnCIG1jlDNLS7JyIZ68QVdqxrzulrrxjd9aFG5Yvt7NE/E0zfuNXj0U45x1xwlrlkqgcCDNqlUUQRUshMwtyXxgsnuLF3M9EreRSBTngGzhgIU8U5DkXVQSVj+iQREtIBZfUSNFdb2pwASB4vTQKzM/B5UuzpDHHXssiF9q15cxRLM+0li2+6xANW1TDd2GDhpXo0Dj7Foy5yHzEXS/uusqZQmyoZPHH4Yj7yaIYJXMOpg++/pTc0nE+olu6RQsc+AhV1iLGe0wVKYtInzFpk9KIfki8LfIc0d5ALrxpGi0sxck3YMxRQft+vaZVOTD3dxBQlTi3hxYk5tmuhG6ZzV+ppq+q6ddqdIYB2y744U2r3hGsofTw65D+qVAew2qfGhiprjx89hMgfDoQg8UYBfkHIN1TT2WIYmh9CRy0y2HzQwaUQ1E4z37S+OjrFIGeJgBws0pttsWlNsA0qYd61RbJDZTM3iQ8coItkxzeQwUEJgokb4DWoWwf9Gz14gfK/t4sK2csZincdUU7hvVmf38H1G5Y8HluWqgHfWBI/YPbc+198Xshfi/F75X4/Sh+KyTx/lEJzPlWw/lizfkCM44fY1wbIQV+rdmUyfAtOHJgEycp4LLnEoDfwE3lswdobT13hSDsC9PutOfa2PE14aocS8kcE0ACnpGR5ssmJtIMIrIAkakUqbeihXcEtmWmbr+FLB3ih6PGFHxV6kTvMFodDZnT2kpDgHYGo/KUJCdIarr1FQ3k2CzL0Klq1LWnSRAx13FIvi/gyGfI7XNGhcVuRbYk4HIC5gJKOLajx4R5CQQO1L8IeFn3DkGj0XcodbcordxjwlHBeyelM6xdHW1U0azn+wJRywsZeGsqZgeDYuw94wLuhGlVmwfC65oApkO474eI14tNjm5EbteB+Cu3mC9ldq8vd2OhVpkQbthmsVs/xMmtiWrKQz65kgCGKVuk4VZ1o8DzFTZolkyboDk2xXJ3EsZB5G+u43VJeYeKvkDB8Scatmb2+ggpTXpHncJ0Qpd5ow5FA1BRgIqPNt4WguoMt3RH/aj0bcpdpBxPJ1K5mp4HdXpmQYjuG94JnoUbc6IKYd6FKDnXtTSK5tqheqABowEN6wIL6pDoyfjiCa/Y4vBfmFTdM6CWnO4rORjh8/abXK7Kc6zR1NKGMKAppib/kXpu4rWtTfhI6+cD5cpTv71j2LpY32Kh5sispH4mOIJNLkhji3F7ha2hbaEg06ubTvfAQueyAO8umqn0Dj6HpXIcIJ4603uKNLkZyie03GeAx4XA49tZGKFc75NzFnDM/vWeO1RxpFFEKa36p9Lb2KCTHimUNDMeaU3K7EOt6lccyEzsA8ZLalX0nNj/zUmF9jhm19+WGamlpGSqz0QZBXJa75Kc9pg61EPf1C4FbJdEjCuXzSiSe5242wLvOnTWz5B1qnP73SBNeTxGUtQz1Ptgt2QaJXERxgteNhFsJXzZoPK1C2epRZLPO6/mTuop6lSqSknECWscu+E7hMkTAcTbnXK+ywQq76TlMoXdiQjKE6J6MVcnlgZ5vuZe92CqSnN073JYGfZUhM5bJMxpkpq0reqj5M0gSt5U12EJb7OfUPIoEkdEGABbHmy+a/t+GIeF7wPpFE0aBMu902pgxWip7AD9v7L+6R2UlvUNn+ketYtQNZ8VBxvbxChFTMPf9ttHN0G0COQ/TOT/i95GwZJnxoOz6uTGg7t62F+tOfnYeHixsgUWiJIRMuHYEHt+EsxCrNy53RXFNQ8KUzVazpd2Y1FzJcACw67vy+/Zvq8RLcvvutcz91xrZ0crbuucY6nBPPn+YHrRfxZMnmUJ+nAV/VuBlGU2Lv9ZOBHeSG7DeGqUe/X+iiUyiAD3jIeXq/9pJGeeqTrJ0uquSK1Q+qyiMtb2/XkQxr7f7pHbXudjssjkrc0or2f1f0+FI1adhh/kZdFq/QMQVcZV')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)
