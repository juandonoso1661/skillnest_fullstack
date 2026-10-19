// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', () => {

  // ==========================================
  // 1. MODO CLARO / OSCURO (CON PERSISTENCIA)
  // ==========================================
  const themeToggleBtn = document.getElementById('theme-toggle');
  const themeIcon = document.getElementById('theme-icon');
  
  // Guardar/Cargar tema desde localStorage
  const savedTheme = localStorage.getItem('portfolio-theme');
  if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark');
    themeIcon.className = 'fas fa-sun text-yellow-400';
  } else {
    document.documentElement.classList.remove('dark');
    themeIcon.className = 'fas fa-moon text-gray-600';
  }

  themeToggleBtn.addEventListener('click', () => {
    document.documentElement.classList.toggle('dark');
    const isDark = document.documentElement.classList.contains('dark');
    themeIcon.className = isDark ? 'fas fa-sun text-yellow-400' : 'fas fa-moon text-gray-600';
    localStorage.setItem('portfolio-theme', isDark ? 'dark' : 'light');
  });

  // ==========================================
  // 2. NAVEGACIÓN Y MENÚ MÓVIL
  // ==========================================
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const mobileLinks = document.querySelectorAll('.mobile-link');

  mobileMenuBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
  });

  mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
      mobileMenu.classList.add('hidden');
    });
  });

  // ==========================================
  // 3. BARRA DE PROGRESO DE SCROLL
  // ==========================================
  const progressBar = document.getElementById('scroll-progress');
  window.addEventListener('scroll', () => {
    const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = (window.scrollY / totalHeight) * 100;
    progressBar.style.width = `${progress}%`;
  });

  // ==========================================
  // 4. FILTRADO DINÁMICO DE PROYECTOS
  // ==========================================
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      // Remover clase 'active' de todos los botones
      filterBtns.forEach(b => b.classList.remove('active', 'bg-blue-600', 'text-white'));
      btn.classList.add('active', 'bg-blue-600', 'text-white');

      const filterValue = btn.getAttribute('data-filter');

      projectCards.forEach(card => {
        const categories = card.getAttribute('data-category').split(' ');
        if (filterValue === 'all' || categories.includes(filterValue)) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // ==========================================
  // 5. VENTANA MODAL PARA PROYECTOS
  // ==========================================
  const modal = document.getElementById('project-modal');
  const closeModalBtn = document.getElementById('close-modal-btn');
  const modalTitle = document.getElementById('modal-title');
  const modalDescription = document.getElementById('modal-description');
  const modalTech = document.getElementById('modal-tech');
  const modalDemo = document.getElementById('modal-demo');
  const modalRepo = document.getElementById('modal-repo');

  document.querySelectorAll('.open-modal-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const card = e.target.closest('.project-card');
      
      modalTitle.textContent = card.getAttribute('data-title');
      modalDescription.textContent = card.getAttribute('data-description');
      modalTech.textContent = card.getAttribute('data-tech');
      modalDemo.setAttribute('href', card.getAttribute('data-demo'));
      modalRepo.setAttribute('href', card.getAttribute('data-repo'));

      modal.classList.add('open');
    });
  });

  closeModalBtn.addEventListener('click', () => {
    modal.classList.remove('open');
  });

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.classList.remove('open');
    }
  });

  // ==========================================
  // 6. ACORDEÓN DE EJERCICIOS ADICIONALES
  // ==========================================
  const accordionHeaders = document.querySelectorAll('.accordion-header');

  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const content = header.nextElementSibling;
      const icon = header.querySelector('i');

      content.classList.toggle('hidden');
      icon.classList.toggle('rotate-180');
    });
  });

  // ==========================================
  // 7. COPIAR CORREO AL PORTAPAPELES
  // ==========================================
  const copyEmailBtn = document.getElementById('copy-email-btn');
  const emailText = document.getElementById('email-text').textContent;

  copyEmailBtn.addEventListener('click', () => {
    navigator.clipboard.writeText(emailText).then(() => {
      const originalText = copyEmailBtn.textContent;
      copyEmailBtn.textContent = '¡Copiado!';
      copyEmailBtn.classList.replace('bg-blue-600', 'bg-green-600');
      
      setTimeout(() => {
        copyEmailBtn.textContent = originalText;
        copyEmailBtn.classList.replace('bg-green-600', 'bg-blue-600');
      }, 2000);
    });
  });

  // ==========================================
  // 8. FORMULARIO DE CONTACTO E INTERACCIÓN
  // ==========================================
  const contactForm = document.getElementById('contact-form');
  const formStatus = document.getElementById('form-status');

  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    // Simulación de envío exitoso
    formStatus.textContent = '¡Gracias por tu mensaje! Te responderé muy pronto.';
    formStatus.className = 'text-sm text-center font-medium mt-2 text-green-600 dark:text-green-400 block';
    
    contactForm.reset();

    setTimeout(() => {
      formStatus.classList.add('hidden');
    }, 4000);
  });

});