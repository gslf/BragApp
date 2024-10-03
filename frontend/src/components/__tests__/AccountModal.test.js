import { mount } from '@vue/test-utils';
import { describe, it, expect } from 'vitest';
import Modal from '@/components/AccountModal.vue';

describe('Modal.vue', () => {
  const account = {
    account_number: '123456',
    account_name: 'John Doe',
    iban: 'IT60X0542811101000000123456',
    address: '123 Main Street',
    amount: '1000 EUR',
    type: 'Personal'
  };

  it('renders account details correctly', () => {
    const wrapper = mount(Modal, {
      props: {
        account
      }
    });

    expect(wrapper.find('.modal-title').text()).toBe('Account Details');
    expect(wrapper.text()).toContain(account.account_number);
    expect(wrapper.text()).toContain(account.account_name);
    expect(wrapper.text()).toContain(account.iban);
    expect(wrapper.text()).toContain(account.address);
    expect(wrapper.text()).toContain(account.amount);
    expect(wrapper.text()).toContain(account.type);
  });

  it('emits close event when close button is clicked', async () => {
    const wrapper = mount(Modal, {
      props: {
        account
      }
    });

    await wrapper.find('.modal-close-button').trigger('click');

    expect(wrapper.emitted()).toHaveProperty('close');
  });

  it('emits close event when clicking on overlay', async () => {
    const wrapper = mount(Modal, {
      props: {
        account
      }
    });

    await wrapper.find('.modal-overlay').trigger('click');

    expect(wrapper.emitted()).toHaveProperty('close');
  });

  it('does not emit close event when modal content is clicked', async () => {
    const wrapper = mount(Modal, {
      props: {
        account
      }
    });

    await wrapper.find('.modal').trigger('click');

    expect(wrapper.emitted().close).toBeUndefined();
  });
});
