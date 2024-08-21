document.addEventListener('DOMContentLoaded', function () {
    const monthYear = document.querySelector('.month-year');
    const prev = document.querySelector('.prev');
    const next = document.querySelector('.next');
    const days = document.querySelector('.days');
    
    let date = new Date();
    let selectedDate;

    function renderCalendar() {
        const month = date.getMonth();
        const year = date.getFullYear();
        const firstDay = new Date(year, month, 1).getDay();
        const lastDate = new Date(year, month + 1, 0).getDate();

        monthYear.textContent = `${year}-${month + 1}`;
        days.innerHTML = '';

        for (let i = 0; i < firstDay; i++) {
            days.innerHTML += `<div></div>`;
        }

        for (let i = 1; i <= lastDate; i++) {
            days.innerHTML += `<div>${i}</div>`;
        }

        document.querySelectorAll('.days div').forEach(day => {
            day.addEventListener('click', function () {
                selectedDate = new Date(year, month, parseInt(this.textContent));
                document.querySelectorAll('.days div').forEach(d => d.classList.remove('active'));
                this.classList.add('active');
                document.getElementById('date').value = this.textContent+'-'+(month+1)+'-'+year;
                
            });
        });
    }

    prev.addEventListener('click', () => {
        date.setMonth(date.getMonth() - 1);
        renderCalendar();
    });

    next.addEventListener('click', () => {
        date.setMonth(date.getMonth() + 1);
        renderCalendar();
    });

    renderCalendar();
});

