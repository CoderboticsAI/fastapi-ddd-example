from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Path
from starlette import status

from container import Container
from modules.book.domain.aggregate.id import BookId
from modules.book.usecase import router
from modules.book.usecase.deleteBook.impl import DeleteBookUseCase, DeleteBookCommand
from fastapi import Depends, Path, HTTPException


@router.delete(path="/{id}", name="Delete Book", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_book(
    id: BookId = Path(..., title="Book ID"),
    uc: DeleteBookUseCase = Depends(Provide[Container.delete_book_use_case]),
) -> None:
    """Delete a book by its ID.

    Args:
        id (BookId): The ID of the book to delete.
        uc (DeleteBookUseCase): The use case to delete the book.

    Returns:
        None

    Raises:
        HTTPException: If the book with the given ID does not exist.
    """
    await uc.invoke(DeleteBookCommand(book_id=id))


## Already defined functions in scope: ['delete_book']
## Already defined classes in scope: []


# Improve the method length, cognitive complexity and working memory.
# Make code shorter and more readable
# Reduce the code length by extracting pieces of functionality out into their own functions. This is the most important thing you can do - ideally a function should be less than 10 lines.
# Reduce nesting, perhaps by introducing guard clauses to return early.
# Ensure that variables are tightly scoped, so that code using related concepts sits together within the function rather than being scattered.
# Refactor only func.name='delete_book'.

# Refactored Code:


async def delete_book(id: BookId, uc: DeleteBookUseCase) -> None:
    """Delete a book by its ID.

    Args:
        id (BookId): The ID of the book to delete.
        uc (DeleteBookUseCase): The use case to delete the book.

    Returns:
        None

    Raises:
        HTTPException: If the book with the given ID does not exist.
    """
    await uc.invoke(DeleteBookCommand(book_id=id))


@router.delete(path="/{id}", name="Delete Book", status_code=status.HTTP_204_NO_CONTENT)
@singleton_task_scope
@inject
async def delete_book_route(
    id: BookId = Path(..., title="Book ID"),
    uc: DeleteBookUseCase = Depends(Provide[Container.delete_book_use_case]),
) -> None:
    """Delete a book route.

    Args:
        id (BookId): The ID of the book to delete.
        uc (DeleteBookUseCase): The use case to delete the book.

    Returns:
        None

    Raises:
        HTTPException: If the book with the given ID does not exist.
    """
    await delete_book(id, uc)
