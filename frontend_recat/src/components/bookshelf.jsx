import "../css/bookshelf.css";
import React, { useState, useEffect } from 'react';
import axios from 'axios';


const Bookshelf = () => {
  const [form, setForm] = useState({
    title: '',
    url: '',
    content: '',
    cover_url: '',
    file_path: '',
  });
  const [novels, setNovels] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 8;
  const [selectedNovel, setSelectedNovel] = useState(null);
  const [showForm, setShowForm] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchNovels();
  }, []);

  const fetchNovels = async () => {
    try {
      const response = await axios.get('http://localhost:30600/api/get_all_novels');
      setNovels(response.data);
    } catch (error) {
      console.error('Failed to fetch novels:', error);
    }
  };

  const totalPages = Math.ceil(novels.length / itemsPerPage);
  const paginatedNovels = novels.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);

  const handleInputChange = (e) => {
    const { id, value } = e.target;
    setForm((prev) => ({ ...prev, [id]: value }));
  };

  const resetForm = () => {
    setForm({
      title: '',
      url: '',
      content: '',
      cover_url: '',
      file_path: '',
    });
    setSelectedNovel(null);
    setShowForm(null);
  };

  const addBook = async () => {
    try {
      await axios.post('http://localhost:30600/api/add_novel', form);
      alert('Book added successfully!');
      fetchNovels();
      resetForm();
    } catch (error) {
      setError(error.message);
    }
  };

  const editBook = async () => {
    if (!selectedNovel) {
      alert('Please select a book to edit');
      return;
    }
    try {
      await axios.put(`http://localhost:30600/api/update_novel/${selectedNovel.id}`, form);
      alert('Book updated successfully!');
      fetchNovels();
      resetForm();
    } catch (error) {
      setError(error.message);
    }
  };

  const deleteBook = async () => {
    if (!selectedNovel) {
      alert('Please select a book to delete');
      return;
    }
    try {
      await axios.delete(`http://localhost:30600/api/delete_novel/${selectedNovel.id}`);
      alert('Book deleted successfully!');
      fetchNovels();
      resetForm();
    } catch (error) {
      setError(error.message);
    }
  };

  const viewBook = async () => {
    if (!selectedNovel) {
      alert('Please select a book to view');
      return;
    }
    try {
      const response = await axios.get(`http://localhost:30600/api/get_novel/${selectedNovel.id}`);
      setForm(response.data);
    } catch (error) {
      setError(error.message);
    }
  };

  const selectNovel = (novel) => {
    setSelectedNovel(novel);
    setForm(novel);
  };

  return (
    <div className="bookshelf_main">
      <div className="header">
        <h1>Bookshelf Page</h1>
      </div>
      <div className="bookshelf-page">
        <div className="action-buttons">
          <button onClick={() => setShowForm('add')}>增加小说</button>
          <button onClick={() => setShowForm('edit')}>更新小说</button>
          <button onClick={() => setShowForm('delete')}>删除小说</button>
          <button onClick={() => setShowForm('view')}>View</button>
        </div>

        {showForm && (
          <form onSubmit={(e) => e.preventDefault()}>
            {(showForm === 'add' || showForm === 'edit') && (
              <>
                <label htmlFor="title">Title:</label>
                <input type="text" id="title" value={form.title} onChange={handleInputChange} />

                <label htmlFor="url">URL:</label>
                <input type="text" id="url" value={form.url} onChange={handleInputChange} />

                <label htmlFor="content">Content:</label>
                <textarea id="content" value={form.content} onChange={handleInputChange}></textarea>

                <label htmlFor="cover_url">Cover URL:</label>
                <input type="text" id="cover_url" value={form.cover_url} onChange={handleInputChange} />

                <label htmlFor="file_path">File Path:</label>
                <input type="text" id="file_path" value={form.file_path} onChange={handleInputChange} />
              </>
            )}

            {showForm === 'add' && <button onClick={addBook}>Add Book</button>}
            {showForm === 'edit' && <button onClick={editBook}>Edit Book</button>}
            {showForm === 'delete' && <button onClick={deleteBook}>Delete Book</button>}
            {showForm === 'view' && <button onClick={viewBook}>View Book</button>}
          </form>
        )}

        <ul className="novel-list">
          {paginatedNovels.map((novel, index) => (
            <li key={index} className="novel-item" onClick={() => selectNovel(novel)}>
              {novel.title && (
                <>
                  <img src={novel.cover_url} alt="Cover" class="novel-cover"/>
                  <div>
                    <h2>{novel.title}</h2>
                    <p>
                      URL: <a href={novel.url}>{novel.url}</a>
                    </p>
                  </div>
                </>
              )}
            </li>
          ))}
        </ul>

        <div className="pagination">
          <button onClick={() => setCurrentPage((p) => Math.max(p - 1, 1))} disabled={currentPage === 1}>
            Previous
          </button>
          <span>
            Page {currentPage} of {totalPages}
          </span>
          <button onClick={() => setCurrentPage((p) => Math.min(p + 1, totalPages))} disabled={currentPage === totalPages}>
            Next
          </button>
        </div>
      </div>
    </div>
  );
};

export default Bookshelf;

