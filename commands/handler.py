import abc


class Handler(abc.ABC):
    _is_executed = False
    _command = None

    @property
    def is_executed(self) -> bool:
        return self._is_executed

    def execute(self) -> None:
        print(f"{self.__class__.__name__}.execute - {self._command}")
        self._execute()
        self._is_executed = True

    
    @abc.abstractmethod
    def _execute(self) -> None:
        pass

class HandlerRollback(Handler):
    def rollback(self) -> None:
        if self.is_executed is True:
            print(f"{self.__class__.__name__}.rollback - {self._command}")
            self._rollback()
            self._is_executed = False
    

    @abc.abstractmethod
    def _rollback(self) -> None:
        pass
